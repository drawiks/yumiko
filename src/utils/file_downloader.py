
from aiogram import Bot
from aiogram.types import Voice

from dlogger import logger

from typing import Optional

class FileDownloader:
    MAX_FILE_SIZE = 25 * 1024 * 1024

    def __init__(self, bot: Bot):
        self._bot = bot

    async def download_voice(self, voice: Voice) -> Optional[bytes]:
        try:
            file = await self._bot.get_file(voice.file_id)
            file_bytes = await self._bot.download_file(file.file_path)
            audio_data = file_bytes.read()

            if len(audio_data) > self.MAX_FILE_SIZE:
                logger.warning(f"File too large: {len(audio_data)} bytes")
                return None

            logger.debug(f"Downloaded voice file: {len(audio_data)} bytes")
            return audio_data
        except Exception as e:
            logger.error(f"Failed to download voice file: {e}")
            return None
