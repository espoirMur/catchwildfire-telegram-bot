from bot.telegram_bot import TelegramBot

if __name__ == '__main__':
    app = TelegramBot()
    app.run(host='localhost', port=8082)
