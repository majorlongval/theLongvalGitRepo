import turtle


class KeyStateChecker:
    def __init__(self, key='Up'):
        self.key = key
        self.key_state = False

    def get_key_state(self):
        return self.key_state

    def set_key_state(self):
        self.key_state = True
