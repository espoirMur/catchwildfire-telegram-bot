from dotenv import load_dotenv
from os import getenv

load_dotenv()

NASA_API_KEY = getenv('NASA_API_KEY')
TELEGRAM_BOT_TOKEN = getenv('TELEGRAM_BOT_TOKEN')
