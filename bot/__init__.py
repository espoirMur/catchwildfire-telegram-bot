import telebot

from config import TELEGRAM_BOT_TOKEN
from functools import partial
from bot.user import User
from bot.messages import send_current_candidate
from landsat import LandsatBisector
from constants import LON, LAT
from config import NASA_API_KEY

bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

user_dict = {}


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bisector = LandsatBisector(LON, LAT)
    indice = 0
    message = send_current_candidate(bot, message, bisector, indice)
    bot.register_next_step_handler(message, partial(process_step, indice, bisector))


def process_step(indice,  bisector, message):
    response = message.text
    user = User.create_get_user(message, bisector=bisector)
    if indice < bisector.count-1:
        indice += 1
        try:
            # get or create
            user.responses[bisector.date] = response
            message = send_current_candidate(bot, message, bisector, indice)
            bot.register_next_step_handler(message, partial(process_step, indice, bisector))
        except Exception as e:
            print(e)
            bot.reply_to(message, 'oooops')
    else:
        ## send peform the algorithms on results and clear everything
        bot.reply_to(message, f'Thanks for using the game {user.responses}')


# Enable saving next step handlers to file "./.handlers-saves/step.save".
# Delay=2 means that after any change in next step handlers (e.g. calling register_next_step_handler())
# saving will hapen after delay 2 seconds.
