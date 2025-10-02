from abc import ABC, abstractmethod
from typing import Any


class LLMClient(ABC):
    # HACK to limit the LLMs to answer only recipes
    # Proper fix would be word embeddings
    GUARDRAIL = "Only answer recipe/cooking questions. For anything else, reply: 'I only prepare recipes.'"

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

    def modify_prompt(self, prompt: str) -> str:
        return f"{prompt}\n\n{self.GUARDRAIL}"