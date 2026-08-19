import os
from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
DB_NAME = os.getenv("DB_NAME", "kotozayats.db")
if not TOKEN:
    raise ValueError("Токен бота не найден")

