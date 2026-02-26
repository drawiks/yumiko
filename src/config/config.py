
from environs import env

env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")
GROQ_API_KEY = env.str("GROQ_API_KEY")

LOG_LEVEL = env.str("LOG_LEVEL", "INFO")
LOG_FILE = env.str("LOG_FILE", "logs/bot.log")
LOG_ROTATION = env.str("LOG_ROTATION", "10MB")
LOG_RETENTION = env.str("LOG_RETENTION", "7 days")
