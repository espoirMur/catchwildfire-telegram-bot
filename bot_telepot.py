import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import TELEGRAM_BOT_TOKEN


bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)


def gen_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("Yes", callback_data="1"),
               InlineKeyboardButton("No", callback_data="0"))
    return markup


def create_inital_marlkup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(InlineKeyboardButton("Yes", callback_data="start"),)
    return markup


