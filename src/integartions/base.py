from abc import ABC, abstractmethod


class LLMClient(ABC):
    @abstractmethod
    def chat(self, prompt: str) -> str:
        """Send a prompt to the LLM and return a response"""
        pass
