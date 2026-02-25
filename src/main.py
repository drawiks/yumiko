
from aiogram.filters.command import Command

from src.core import dp, get_bot
from src.handlers import cmd_start, cmd_help, handle_voice

from src.config import LOG_LEVEL, LOG_FILE, LOG_ROTATION, LOG_RETENTION

from dlogger import logger

from pathlib import Path
import asyncio

def setup_logging():
    log_path = Path(LOG_FILE)
    log_path.parent.mkdir(parents=True, exist_ok=True)

    logger.configure(
        level=LOG_LEVEL,
        log_file=LOG_FILE,
        rotation=LOG_ROTATION,
        retention=LOG_RETENTION,
    )

def register_handlers():
    dp.message.register(cmd_start, Command("start"))
    dp.message.register(cmd_help, Command("help"))
    dp.message.register(handle_voice)

async def main():
    setup_logging()
    logger.info("Starting bot...")

    register_handlers()

    bot = get_bot()
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
