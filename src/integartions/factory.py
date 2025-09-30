from base import LLMClient
from chatgpt import ChatGPTClient
from gemini import GeminiClient

from settings import get_settings


class LLMFactory:
    _registry = {
        "ChatGPT": ChatGPTClient,
        "Gemini": GeminiClient,
    }

    @staticmethod
    def create_llm(llm_name: str) -> LLMClient:
        settings = get_settings()
        api_keys = {
            "ChatGPT": settings.openai_api_key,
            "Gemini": settings.gemini_api_key,
        }

        if llm_name not in LLMFactory._registry:
            raise ValueError(f"Unsupported LLM: {llm_name}")

        return LLMFactory._registry[llm_name](api_keys[llm_name])
