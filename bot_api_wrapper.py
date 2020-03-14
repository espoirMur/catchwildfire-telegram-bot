import telegram
from io import BytesIO
from telegram import InlineKeyboardButton, InlineKeyboardMarkup


class MyTelegramBot(telegram.Bot):
    def __init__(self, token):
        super().__init__(token=token)

    def build_inline_keyboard(self):
        """
        Build the bot keyboard that will send actions to user
        return : The bot keyboard
        """
        keyboard = [[InlineKeyboardButton("Yes", callback_data='1'),
                     InlineKeyboardButton("No", callback_data='0')]]

        reply_markup = InlineKeyboardMarkup(keyboard)
        return reply_markup

    def send_message_with_picture(self, chat_id, picture, date):
        """
        Send message with the picture to the user with
        Args:
            bot ([type]): [description]
            picture ([type]): [description]
            date : bisector date
        """
        reply_markup = self.build_inline_keyboard()
        self.send_photo(
            chat_id,
            photo=open('./images/image_2020.png', 'rb'),
            reply_markup=reply_markup,
            caption=f'Did you see it?{date}')

    def get_chat_id(self):
        """
        return the chat id from the given bot
        """
        self.get_updates()[-1].message.chat_id
