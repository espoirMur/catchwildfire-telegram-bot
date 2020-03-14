from PyInquirer import prompt


def bisect(n, mapper, tester):
    """
    Runs a bisection.

    - `n` is the number of elements to be bisected
    - `mapper` is a callable that will transform an integer from "0" to "n"
      into a value that can be tested
    - `tester` returns true if the value is within the "right" range
    """

    if n < 1:
        raise ValueError('Cannot bissect an empty array')

    left = 0
    right = n - 1

    while left + 1 < right:
        mid = int((left + right) / 2)

        val = mapper(mid)

        if tester(val):
            right = mid
        else:
            left = mid

    return mapper(right)


def confirm(title):
    """
    Asks a yes/no question to the user
    """

    return prompt([{
        'type': 'confirm',
        'name': 'confirm',
        'message': f'{title} - do you see it?',
    }])['confirm']


def display_current_canditate(candidate, bisector, bot):
    """
    Displays the current candidate to the user and asks them to
    check if they see wildfire damages.
    candidate : the candidate to display
    bisector : the bisector instance
    bot: the telegram bot
    """

    bisector.index = candidate
    chat_id = bot.get_updates()[-1].message.chat_id
    image = bisector.image.save_image()
    bot.send_message_with_picture(
        chat_id=chat_id,
        picture=bisector.image,
        date=bisector.date)
    # should return the selcted action from users
    return True
