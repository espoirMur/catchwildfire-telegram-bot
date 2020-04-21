from telebot.types import ReplyKeyboardMarkup


def build_reply_markup():
    """
    Build the telegram reply markup
    return : the reply keyboard markup object
    """
    markup = ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.add('Yes', 'No')
    return markup


def send_current_candidate(bot, message, bisector, current_canditate_index):
    """
    Displays the current candidate to the user and asks them to
    check if they see wildfire damages.
    current_canditate_index : the index candidate to display
    bisector : the bisector instance
    bot: the telegram bot
    message: the message we are replying to
    """
    markup = build_reply_markup()
    bisector.index = current_canditate_index
    chat_id = message.chat.id
    message = bot.send_photo(
        chat_id=chat_id,
        photo=bisector.image.generate_image_bytes(),
        caption=f"{bisector.index} - did the rocket launch yet?",
        reply_markup=markup)
    return message
