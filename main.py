from constants import LON, LAT
from landsat import LandsatBisector
from actions import bisect
from functools import partial
from config import NASA_API_KEY, TELEGRAM_BOT_TOKEN
from bot_telepot import bot, gen_markup, create_inital_marlkup

bisector = None
chat_id = ''


if __name__ == '__main__':
    bot.enable_save_next_step_handlers(delay=2)

    # Load next_step_handlers from save file (default "./.handlers-saves/step.save")
    # WARNING It will work only if enable_save_next_step_handlers was called!
    bot.load_next_step_handlers()

    bot.polling()
