
from aiogram import types

from dlogger import logger

async def cmd_start(message: types.Message):
    logger.info(f"User {message.from_user.id} started bot")
    await message.answer("Привет! Отправь мне голосовое сообщение, и я переведу его в текст.")

async def cmd_help(message: types.Message):
    await message.answer("Просто отправь мне голосовое сообщение, и я переведу его в текст.")
