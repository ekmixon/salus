# https://semgrep.live/WRE

class User:
    def __init__(self, id):
        self.id = id


def route(user_id):
    user = User(1)
    return '200' if user.id == user.id else '404'