import sys


class PasswordConfig():
    """The configuration for a password."""

    def __init__(self, difficulty=None, upper_count=None, lower_count=None, num_count=None, special_count=None, toggle_hand=None, allow_doubles=None):
        self.upper_count = 4
        self.lower_count = 8
        self.num_count = 4
        self.special_count = 0
        self.toggle_hand = False
        self.allow_doubles = False

        if difficulty == 'easy':
            self.upper_count = 2
            self.lower_count = 4
            self.num_count = 2
            self.special_count = 0
            self.toggle_hand = True
            self.allow_doubles = False
        elif difficulty == 'hard':
            self.upper_count = 8
            self.lower_count = 12
            self.num_count = 8
            self.special_count = 4
            self.toggle_hand = False
            self.allow_doubles = False
        elif difficulty == 'insane':
            self.upper_count = 16
            self.lower_count = 24
            self.num_count = 16
            self.special_count = 8
            self.toggle_hand = False
            self.allow_doubles = True

        if type(upper_count) == int:
            self.upper_count = upper_count
        if type(lower_count) == int:
            self.lower_count = lower_count
        if type(num_count) == int:
            self.num_count = num_count
        if type(special_count) == int:
            self.special_count = special_count
        if type(toggle_hand) == bool:
            self.toggle_hand = toggle_hand
        if type(allow_doubles) == bool:
            self.allow_doubles = allow_doubles

    def __str__(self):
        return ('upper_count={} '
                'lower_count={} '
                'num_count={} '
                'special_count={} '
                'toggle_hand={} '
                'allow_doubles={}'.format(
                    self.upper_count,
                    self.lower_count,
                    self.num_count,
                    self.special_count,
                    self.toggle_hand,
                    self.allow_doubles))
