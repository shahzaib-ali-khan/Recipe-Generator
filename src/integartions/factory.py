from src.integartions.base import LLMClient
from src.integartions.chatgpt import ChatGPTClient
from src.integartions.gemini import GeminiClient
from src.settings import Settings, get_settings


class LLMFactory:
    _registry = {
        "ChatGPT": ChatGPTClient,
        "Gemini": GeminiClient,
    }

    def __init__(self, settings: Settings | None = None):
        self._settings = settings or get_settings()

    def get_model_variant(self, llm_name: str) -> str:
        model_variants_mapping = {
            "ChatGPT": self._settings.openai_model_variant,
            "Gemini": self._settings.gemini_model_variant,
        }
        return model_variants_mapping[llm_name]

    def get_api_key(self, llm_name: str) -> str:
        api_keys = {
            "ChatGPT": self._settings.openai_api_key,
            "Gemini": self._settings.gemini_api_key,
        }
        key = api_keys.get(llm_name, None)
        if not key:
            raise KeyError(f"No API key found for {llm_name}")
        return key

    def create_llm(self, llm_name: str) -> LLMClient:
        if llm_name not in LLMFactory._registry:
            raise ValueError(f"Unsupported LLM: {llm_name}")

        return LLMFactory._registry[llm_name](
            self.get_api_key(llm_name), self.get_model_variant(llm_name)
        )
