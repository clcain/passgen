from random import SystemRandom

from password_char import Char
from password_char import Upper
from password_char import Lower
from password_char import Num
from password_char import Special

def generate_password(config):
    """Generate a password using the specified config.

    Args:
        config: The configuration object specifying the parameters
                for this password.
    Returns:
        A complete password in string format.
    """

    Char.set_config(config)

    password_types = []
    for i in range(0, config.upper_count):
        password_types.append(Upper())
    for i in range(0, config.lower_count):
        password_types.append(Lower())
    for i in range(0, config.num_count):
        password_types.append(Num())
    for i in range(0, config.special_count):
        password_types.append(Special())
    SystemRandom().shuffle(password_types)

    password = []
    for i in password_types:
        password.append(str(i))

    return ''.join(password)
