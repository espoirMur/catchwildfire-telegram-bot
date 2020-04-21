import telebot
from config import TELEGRAM_BOT_TOKEN, VIDEO_NAME
from functools import partial
from bot.user import User, user_dict
from bot.messages import send_current_candidate
from frame import FrameXBisector
from actions import tester_function, bisect


bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    # how to handle loading...
    bisector = FrameXBisector(VIDEO_NAME)
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
            user.responses[bisector._index] = response
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
        bot.reply_to(message, f"Found! First apparition = {bisector.index}")
        # TODO: delete the user from the user dict
        del user_dict[message.from_user.id]
