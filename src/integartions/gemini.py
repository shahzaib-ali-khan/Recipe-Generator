from google import genai
from google.genai import Client
from google.genai.types import GenerateContentResponse

from src.integartions.base import LLMClient


class GeminiClient(LLMClient):
    def __init__(self, api_key: str, model_variant: str):
        self._model_variant = model_variant
        self._api_key = api_key
        self._client: Client | None = None  # cache the client

    def get_client(self) -> Client:
        if self._client is None:
            self._client = genai.Client(api_key=self._api_key)
        return self._client

    def get_response(self, input_text: str) -> GenerateContentResponse:
        return self.get_client().models.generate_content(
            model=self._model_variant,
            contents=input_text,
        )

    def text_response(self, input_text: str) -> str:
        response = self.get_response(input_text)
        return response.text

    def chat(self, prompt: str) -> str:
        return self.text_response(super().modify_prompt(prompt))
