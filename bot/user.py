from itertools import repeat

user_dict = {}


class User:
    def __init__(self, name, indexes=[]):
        """users with name
        Args:
            name ([type]): [description]
            dates (list, optional): date of bisector
        """
        self.name = name
        self.age = None
        self.sex = None
        self.responses = dict(zip(indexes, repeat(None)))

    @staticmethod
    def create_get_user(message, bisector):
        """
        check in the user dictionary and create users if not exist
        message :telegram message
        bisector : landstat bisector instance
        """
        user_id = message.from_user.id
        if user_dict.get(user_id):
            user = user_dict.get(user_id)
        else:
            indexes = range(bisector.video.frames)
            user = User(user_id, indexes=indexes)
            user_dict[user_id] = user
        return user
