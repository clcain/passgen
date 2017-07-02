from random import SystemRandom

class Char():
    """The base class for an object representation of the different types of
       items that may be combined to form a password."""

    @staticmethod
    def set_config(config):
        """Set the config of the Char class so that when str() is called
           on an instance of this object, the output will adhere to the
           specified parameters.

        Args:
            config: The password configuration object.
        """

        Char.random = SystemRandom()
        Char.toggle_hand = config.toggle_hand
        Char.allow_doubles = config.allow_doubles
        Char.previous_char = None
        Char.left = Char.random.random() > .5

    def get_next(self):
        """Get the next manifestation of this type of password item.

        Returns:
            The next manifestation of this type of password item.
        """

        next_char = None
        complete = False

        while not complete:
            if Char.toggle_hand:
                if Char.left:
                    next_char = self._get_left()
                else:
                    next_char = self._get_right()
            else:
                if Char.random.random() > .5:
                    next_char = self._get_left()
                else:
                    next_char = self._get_right()
            if Char.allow_doubles or next_char is not Char.previous_char:
                complete = True

        Char.previous_char = next_char
        Char.left = not Char.left
        return next_char

    def _get_left(self):
        return Char.random.choice(self.left_list)

    def _get_right(self):
        return Char.random.choice(self.right_list)

    def __str__(self):
        return self.get_next()

class Upper(Char):
    """The upper case letter type."""

    def __init__(self):
        self.left_list = ['Q', 'W', 'E', 'R', 'T', 'A', 'S', 'D', 'F', 'G', 'Z', 'X', 'C', 'V']
        self.right_list = ['Y', 'U', 'I', 'O', 'P', 'H', 'J', 'K', 'L', 'B', 'N', 'M']


class Lower(Char):
    """The lower case letter type."""

    def __init__(self):
        self.left_list = ['q', 'w', 'e', 'r', 't', 'a', 's', 'd', 'f', 'g', 'z', 'x', 'c', 'v']
        self.right_list = ['y', 'u', 'i', 'o', 'p', 'h', 'j', 'k', 'l', 'b', 'n', 'm']

class Num(Char):
    """The number type."""

    def __init__(self):
        self.left_list = ['1', '2', '3', '4', '5']
        self.right_list = ['6', '7', '8', '9', '0']

class Special(Char):
    """The special character type."""

    def __init__(self):
        self.left_list = ['!', '@', '#', '$', '%']
        self.right_list = ['^', '&', '*', '(', ')']
