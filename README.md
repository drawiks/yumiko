<div align="center">
    <h1>👾 yumiko</h1>
    <img height="20" alt="Python 3.11+" src="https://img.shields.io/badge/python-3.11+-blue">
    <img height="20" alt="License MIT" src="https://img.shields.io/badge/license-MIT-green">
    <img height="20" alt="Status" src="https://img.shields.io/badge/status-stable-red">
    <p><strong>yumiko</strong> — telegram-бот для преобразования голосовых сообщений в текст</p>
    <blockquote>(─‿‿─)</blockquote>
</div>

---

```
 __    __                       __
/\ \  /\ \                   __/\ \
\ `\`\\/'/__  __    ___ ___ /\_\ \ \/'\     ___
 `\ `\ /'/\ \/\ \ /' __` __`\/\ \ \ , <    / __`\
   `\ \ \\ \ \_\ \/\ \/\ \/\ \ \ \ \ \\`\ /\ \L\ \
     \ \_\\ \____/\ \_\ \_\ \_\ \_\ \_\ \_\ \____/
      \/_/ \/___/  \/_/\/_/\/_/\/_/\/_/\/_/\/___/
```

## **📂 структура проекта**

```bash
yumiko/
│
├── src/
│   ├── config/
│   │   ├── __init__.py
│   │   └── config.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── abstract.py          # --- абстрактный класс stt сервиса ---
│   │   └── groq_stt.py         # --- groq api ---
│   ├── handlers/
│   │   ├── __init__.py
│   │   ├── commands.py
│   │   └── voice.py           # --- обработка голосовых ---
│   ├── core/
│   │   ├── __init__.py
│   │   ├── bot.py             # --- инициализация бота ---
│   │   └── registry.py        # --- DI контейнер ---
│   ├── utils/
│   │   ├── __init__.py
│   │   └── file_downloader.py # --- загрузка файлов ---
│   │
│   └── main.py
│
├── yumiko.py # --- entrypoint ---
│
├── .env
├── .env.example
├── requirements.txt
├── README.md
└── LICENSE
```

[src/main.py](/src/main.py)
```python
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
```

---

## **🧩 зависимости**
[requirements.txt](/requirements.txt)
```bash
# --- bot ---
aiogram==3.25.0

# --- web ---
aiohttp==3.11.11

# --- config ---
environs==14.6.0

# --- logs ---
dlogger-drawiks==0.2.2
```
