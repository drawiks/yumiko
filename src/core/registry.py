
from aiogram import Bot

from src.services import AbstractSTTService, GroqSTTService
from src.utils import FileDownloader

from src.config import BOT_TOKEN

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.services import AbstractSTTService

class Registry:
    _instance = None

    def __init__(self):
        self._bot: Bot | None = None
        self._stt_service: AbstractSTTService | None = None
        self._file_downloader: FileDownloader | None = None

    @classmethod
    def get_instance(cls) -> "Registry":
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    @property
    def bot(self) -> Bot:
        if self._bot is None:
            self._bot = Bot(token=BOT_TOKEN)
        return self._bot

    @property
    def stt_service(self) -> AbstractSTTService:
        if self._stt_service is None:
            self._stt_service = GroqSTTService()
        return self._stt_service

    @property
    def file_downloader(self) -> FileDownloader:
        if self._file_downloader is None:
            self._file_downloader = FileDownloader(self.bot)
        return self._file_downloader

def get_registry() -> Registry:
    return Registry.get_instance()
