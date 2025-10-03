from functools import lru_cache

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Recipe Generator"
    supported_llms: list[str] = ["ChatGPT", "Gemini"]
    openai_api_key: str = ""
    openai_model_variant: str = "gpt-4.1"
    gemini_api_key: str = ""
    gemini_model_variant: str = "gemini-2.5-flash"


@lru_cache
def get_settings():
    return Settings()