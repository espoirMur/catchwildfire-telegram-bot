import telebot
from config import TELEGRAM_BOT_TOKEN, VIDEO_NAME
from functools import partial
from bot.messages import send_current_candidate
from frame import FrameXBisector


bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    # how to handle loading...
    bisector = FrameXBisector(VIDEO_NAME)
    left = 0
    right = bisector.count - 1
    mid = int((left + right) / 2)
    message = send_current_candidate(bot, message, bisector, mid)
    bot.register_next_step_handler(
        message, partial(
            process_step, left, right, bisector))


def process_step(left, right, bisector, message):
    """
    Process the next step while running bisection

    Args:
        left ([type]): [description]
        right ([type]): [description]
        bisector ([type]): [description]
        message ([type]): [description]
    """
    response = message.text
    if left + 1 < right:
        try:
            mid = int((left + right) / 2)
            message = send_current_candidate(bot, message, bisector, mid)
            if response.lower() == 'yes':
                right = mid
            else:
                left = mid
            bot.register_next_step_handler(
                message, partial(
                    process_step, left, right, bisector))
        except Exception as e:
            print(e)
            bot.reply_to(message, 'oooops, Are you sure you selected yes or no?')
    else:
        culprit = right
        bisector.index = culprit
        bot.reply_to(message, f"Found! First apparition = {bisector.index}")
