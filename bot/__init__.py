import telebot

from config import TELEGRAM_BOT_TOKEN
from functools import partial
from bot.user import User
from bot.messages import send_current_candidate
from landsat import LandsatBisector
from constants import LON, LAT
from config import NASA_API_KEY
from actions import tester_function, bisect

bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

user_dict = {}


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    # how to handle loading...
    bisector = LandsatBisector(LON, LAT)
    indice = 0
    message = send_current_candidate(bot, message, bisector, indice)
    bot.register_next_step_handler(
        message, partial(
            process_step, indice, bisector))


def process_step(indice, bisector, message):
    response = message.text
    user = User.create_get_user(message, bisector=bisector)
    if indice < bisector.count - 1:
        indice += 1
        try:
            # get or create
            user.responses[bisector.date] = response
            message = send_current_candidate(bot, message, bisector, indice)
            bot.register_next_step_handler(
                message, partial(
                    process_step, indice, bisector))
        except Exception as e:
            print(e)
            bot.reply_to(message, 'oooops')
    else:
        culprit = bisect(bisector.count,
                         lambda x: x,
                         partial(
                             tester_function,
                             responses=list(user.responses.values())))
        bisector.index = culprit
        bot.reply_to(message, f"Found! First apparition = {bisector.date}")
