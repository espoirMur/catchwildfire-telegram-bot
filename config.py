from dotenv import load_dotenv
from os import getenv

load_dotenv()

API_BASE = getenv("API_BASE")
VIDEO_NAME = getenv("VIDEO_NAME")
TELEGRAM_BOT_TOKEN = getenv('TELEGRAM_BOT_TOKEN')
