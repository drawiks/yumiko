
import aiohttp

from src.config import GROQ_API_KEY
from src.services import AbstractSTTService

from dlogger import logger

from typing import Optional

class GroqSTTService(AbstractSTTService):
    URL = "https://api.groq.com/openai/v1/audio/transcriptions"
    MODEL = "whisper-large-v3"

    def __init__(self, api_key: str = GROQ_API_KEY):
        self._api_key = api_key
        self._url = self.URL
        self._model = self.MODEL

    async def transcribe(self, audio_data: bytes, filename: str = "voice.ogg") -> Optional[str]:
        try:
            async with aiohttp.ClientSession() as session:
                form = aiohttp.FormData()
                form.add_field(
                    "file",
                    audio_data,
                    filename=filename,
                    content_type="audio/ogg"
                )
                form.add_field("model", self._model)
                form.add_field("language", "ru")
                form.add_field("response_format", "json")

                headers = {"Authorization": f"Bearer {self._api_key}"}

                async with session.post(self._url, data=form, headers=headers) as resp:
                    if resp.status == 200:
                        result = await resp.json()
                        text = result.get("text", "").strip()
                        logger.info(f"transcription successful: {text[:50]}...")
                        return text

                    error_text = await resp.text()
                    logger.error(f"groq api error {resp.status}: {error_text}")
                    return None
        except Exception as e:
            logger.error(f"transcription failed: {e}")
            return None
