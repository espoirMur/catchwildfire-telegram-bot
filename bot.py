from config import TELEGRAM_BOT_TOKEN
import logging

from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)
logger = logging.getLogger(__name__)


def start(update, context):
    """
    When a user click start it start the bot and display the
    keyboard when he will reply by yes or now

    Args:
        bot: the bot instance
        context: context instance
    """
    keyboard = [[InlineKeyboardButton("Yes", callback_data='1'),
                 InlineKeyboardButton("No", callback_data='0')]]

    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.send_photo(update.effective_chat.id,
                           open('images/my_avatar.png', 'rb'))
    update.message.reply_text('Did you see it?:', reply_markup=reply_markup)


def button(update, context):
    """
    Handle the reply and send back the message to the user

    Args:
        update ([type]): [description]
        context ([type]): [description]
    """
    query = update.callback_query

    query.edit_message_text(text="Selected option: {}".format(query.data))


def help(update, context):
    update.message.reply_text("Use /start to test this bot.")


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    updater = Updater(TELEGRAM_BOT_TOKEN, use_context=True)

    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CallbackQueryHandler(button))
    updater.dispatcher.add_handler(CommandHandler('help', help))
    updater.dispatcher.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT
    updater.idle()


if __name__ == '__main__':
    main()
