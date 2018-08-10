import sys

class PasswordConfig():
    """The configuration for a password."""

    def __init__(self, upper_count=2, lower_count=4, num_count=2, special_count=0, toggle_hand=True, allow_doubles=False, human=False):
        self.upper_count = upper_count
        self.lower_count = lower_count
        self.num_count = num_count
        self.special_count = special_count
        self.toggle_hand = toggle_hand
        self.allow_doubles = allow_doubles
        self.human = human
        self.alpha_length = upper_count + lower_count + special_count
        self.total_length = upper_count + lower_count + num_count + special_count

    def __str__(self):
        return ('upper_count={0} '
                'lower_count={1} '
                'num_count={2} '
                'special_count={3} '
                'toggle_hand={4} '
                'allow_doubles={5} '
                'human={6} '.format(
                    self.upper_count,
                    self.lower_count,
                    self.num_count,
                    self.special_count,
                    self.toggle_hand,
                    self.allow_doubles,
                    self.human))
