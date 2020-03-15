from constants import LON, LAT
from landsat import LandsatBisector
from actions import bisect, display_current_canditate
from functools import partial
from config import NASA_API_KEY, TELEGRAM_BOT_TOKEN
from bot_telepot import bot, gen_markup, create_inital_marlkup

bisector = None
chat_id = ''

@bot.callback_query_handler(func=lambda call: True)
def main(call, bisector=bisector, chat_id=chat_id):
    """
    Runs a bisection algorithm on a series of Landsat pictures in order
    for the user to find the approximative date of the fire.

    Images are displayed using pygame, but the interactivity happens in
    the terminal as it is much easier to do.
    """
    
    print('call data is ', call.data, call.data == 'start')

    def tester(n, bisector, chat_id):
        """
        Displays the current candidate to the user and asks them to
        check if they see wildfire damages.
        """
        print('call......')
        bisector.index = n
        bot.send_photo(
            chat_id=chat_id,
            photo=bisector.image.save_image(),
            caption=f"Did you see it Yes or No {bisector.date}",
            reply_markup=gen_markup())
        return eval(call.data)
    # TODO : change this condition
    if call.data != 'start':
        culprit = bisect(bisector.count, lambda x: x, tester)
        bisector.index = culprit
        bot.send_message(chat_id, f"Found! First apparition = {bisector.date}")
    else:
        bisector = LandsatBisector(LON, LAT)
        chat_id = call.message.chat.id

@bot.message_handler(commands=['start', 'help'])
def message_handler(message):
    bot.send_message(message.chat.id, "Yes/no?", reply_markup=create_inital_marlkup())


bot.polling(none_stop=True)
