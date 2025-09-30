from base import LLMClient


class GeminiClient(LLMClient):
    def __init__(self, api_key: str):
        self.api_key = api_key

    def chat(self, prompt: str) -> str:
        return f"Gemini response to: {prompt}"
