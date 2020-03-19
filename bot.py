from config import TELEGRAM_BOT_TOKEN
from itertools import repeat
from functools import partial

bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

user_dict = {}


class User:
    def __init__(self, name):
        self.name = name
        self.age = None
        self.sex = None
        self.response = dict(zip(range(0, 7),  repeat(None)))


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.add('Yes', 'No')
    indice = 0
    message = bot.reply_to(message, f'Did You see it? {0}', reply_markup=markup)
    bot.register_next_step_handler(message, partial(process_step, indice))


def process_step(indice, message):
    user_id = message.from_user.id
    response = message.text
    if user_dict.get(user_id):
        user = user_dict.get(user_id)
    else:
        user = User(user_id)
        user_dict[user_id] = user
    if indice < 7:
        indice += 1
        try:
            # get or create
            user.response[indice] = response
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
            markup.add('Yes', 'No')
            message = bot.reply_to(message, f'Did You see it? {indice}', reply_markup=markup)
            bot.register_next_step_handler(message, partial(process_step, indice))
        except Exception as e:
            bot.reply_to(message, 'oooops')
    else:
        ## send peform the algorithms on results and clear everything
        bot.reply_to(message, f'Thanks for using the game {user.response}')


# Enable saving next step handlers to file "./.handlers-saves/step.save".
# Delay=2 means that after any change in next step handlers (e.g. calling register_next_step_handler())
# saving will hapen after delay 2 seconds.
bot.enable_save_next_step_handlers(delay=2)

# Load next_step_handlers from save file (default "./.handlers-saves/step.save")
# WARNING It will work only if enable_save_next_step_handlers was called!
bot.load_next_step_handlers()

bot.polling()
