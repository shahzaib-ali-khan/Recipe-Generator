from base import LLMClient


class ChatGPTClient(LLMClient):
    def __init__(self, api_key: str):
        self.api_key = api_key

    def chat(self, prompt: str) -> str:
        return f"ChatGPT response to: {prompt}"
