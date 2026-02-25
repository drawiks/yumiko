
from aiogram import Dispatcher

from src.core.registry import get_registry

_registry = get_registry()

bot = _registry.bot
dp = Dispatcher()

def get_bot():
    return _registry.bot

def get_dispatcher() -> Dispatcher:
    return dp
