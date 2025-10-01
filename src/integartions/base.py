from abc import ABC, abstractmethod
from typing import Any


class LLMClient(ABC):
    @abstractmethod
    def get_client(self) -> Any:
        pass

    @abstractmethod
    def get_response(self, input_text: str) -> Any:
        pass

    @abstractmethod
    def text_response(self, input_text: str) -> str:
        pass

    @abstractmethod
    def chat(self, prompt: str) -> str:
        """Send a prompt to the LLM and return a response"""
        pass
