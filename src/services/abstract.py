
from abc import ABC, abstractmethod
from typing import Optional

class AbstractSTTService(ABC):
    @abstractmethod
    async def transcribe(self, audio_data: bytes, filename: str) -> Optional[str]:
        pass
