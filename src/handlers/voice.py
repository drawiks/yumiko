
from aiogram import types

from src.core import get_registry

from dlogger import logger

async def handle_voice(message: types.Message):
    if not message.voice:
        await message.answer("Пожалуйста, отправь голосовое сообщение.")
        return

    registry = get_registry()
    processing_msg = await message.answer("🎤 Обрабатываю голосовое сообщение...")

    try:
        audio_data = await registry.file_downloader.download_voice(message.voice)
        if audio_data is None:
            await processing_msg.edit_text("❌ Не удалось загрузить файл. Попробуйте ещё раз.")
            return

        text = await registry.stt_service.transcribe(audio_data, "voice.ogg")

        if text:
            await processing_msg.edit_text(f"📝 Распознанный текст:\n\n{text}")
            logger.info(f"User {message.from_user.id}: transcribed {len(text)} chars")
        else:
            await processing_msg.edit_text("❌ Не удалось распознать текст. Попробуйте ещё раз.")
    except Exception as e:
        logger.error(f"Error processing voice: {e}")
        await processing_msg.edit_text("❌ Произошла ошибка при обработке. Попробуйте позже.")
