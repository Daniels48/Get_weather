import os
from pathlib import Path

from dotenv import load_dotenv


BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(BASE_DIR / ".env")


BOT_TOKEN = os.getenv("TOKEN")
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")


if not BOT_TOKEN:
    raise ValueError("Не задан TOKEN. Проверь файл .env в корне проекта.")

if not OPENWEATHER_API_KEY:
    raise ValueError("Не задан OPENWEATHER_API_KEY. Проверь файл .env в корне проекта.")