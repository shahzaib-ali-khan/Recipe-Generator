from openai import OpenAI
from openai.types.responses import Response

from src.integartions.base import LLMClient


class ChatGPTClient(LLMClient):
    def __init__(self, api_key: str, model_variant: str, max_retries: int = 2):
        self._model_variant = model_variant
        self._api_key = api_key
        self._max_retries = max_retries
        self._client: OpenAI | None = None  # cache the client

    def get_client(self) -> OpenAI:
        if self._client is None:
            self._client = OpenAI(api_key=self._api_key, max_retries=self._max_retries)
        return self._client

    def get_response(self, input_text: str) -> Response:
        return self.get_client().responses.create(
            model=self._model_variant,
            input=input_text,
        )

    def filter_response_object(self, response: Response) -> str:
        result = ""
        for response in response.output:
            if response.get("type") == "message":
                contents = response.get("contents")
                for content in contents:
                    if content.get("type") == "output_text":
                        result = content.get("text")
                        return result
        return result

    def text_response(self, input_text: str) -> str:
        response = self.get_response(input_text)
        return self.filter_response_object(response)

    def chat(self, prompt: str) -> str:
        return self.text_response(super().modify_prompt(prompt))
