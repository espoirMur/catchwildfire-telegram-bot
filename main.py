from constants import LON, LAT
from landsat import LandsatBisector
from actions import bisect, display_current_canditate
from functools import partial
from config import NASA_API_KEY, TELEGRAM_BOT_TOKEN
from bot_api_wrapper import MyTelegramBot


# keep only main here
def main():
    """
    Runs a bisection algorithm on a series of Landsat pictures in order
    for the user to find the approximates date of the fire.

    Images are displayed using pygame, but the interactivity happens in
    the terminal as it is much easier to do.
    """
    bot = MyTelegramBot(TELEGRAM_BOT_TOKEN)
    chat_id = bot.get_updates()[-1].message.chat_id
    bisector = LandsatBisector(LON, LAT)
    print(bisector.count, '====')
    culprit = bisect(
        bisector.count,
        lambda x: x,
        partial(
            display_current_canditate,
            bisector=bisector,
            bot=bot))
    bisector.index = culprit
    bot.send_message(chat_id=chat_id,
                     text=f"Found! First apparition = {bisector.date}")
    exit()


if __name__ == '__main__':
    main()
