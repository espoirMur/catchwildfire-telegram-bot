# Catching wildfires with bisection
 
 This is a telegram bot that use bisection algorithm to detect wildfires from images.

 It will show different images to the user, asking if they can see wildfire damages on the picture. Based on the answers, it will use a bisection algorithm to find the first image where the wildfire damages appear, helping to pinpoint its occurrence date. Within 5 iterations, it will tell you which is the first image displaying wildfire damages.

## Motivation

This was given as test for software Engineer role.

## Bot link

The bot can be found [here](https://web.telegram.org/#/im?p=@catch_wildfires_bot)

## Tech/framework used

<b>Built with</b>

- Python
- PyTelegramBot
- Flask

## Command 

The bot works for now with  2 commands 

`/start` and `/help`


## Installation

    $ git clone https://github.com/espoirMur/catchwildfire-telegram-bot.git
    $ cd catchwildfire-telegram-bot
    $ pip install -r requirements.txt

Create .env file
create a .env and add the following elements
```
NASA_API_KEY=''
TELEGRAM_BOT_TOKEN=''

```


## Start & watch

    $ python main.py


## License

Espoir © [espoirMur](./LICENCE.md)
