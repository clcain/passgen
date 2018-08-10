#! /usr/bin/python

import sys

import password_generator

from password_config import PasswordConfig

def main():
    config = PasswordConfig()
    try:
        if sys.argv[1] == 'easy':
            config.upper_count = 2
            config.lower_count = 4
            config.num_count = 2
            config.special_count = 0
            config.toggle_hand = True
            config.allow_doubles = False
            config.human = False

        elif sys.argv[1] == 'medium':
            config.upper_count = 4
            config.lower_count = 8
            config.num_count = 4
            config.special_count = 0
            config.toggle_hand = True
            config.allow_doubles = False
            config.human = False

        elif sys.argv[1] == 'hard':
            config.upper_count = 8
            config.lower_count = 12
            config.num_count = 8
            config.special_count = 4
            config.toggle_hand = False
            config.allow_doubles = True
            config.human = False

        elif sys.argv[1] == 'insane':
            config.upper_count = 16
            config.lower_count = 24
            config.num_count = 16
            config.special_count = 8
            config.toggle_hand = False
            config.allow_doubles = True
            config.human = False

        elif sys.argv[1] == 'human':
            config.upper_count = 0
            config.lower_count = 6
            config.num_count = 3
            config.special_count = 0
            config.toggle_hand = True
            config.allow_doubles = False
            config.human = True

        else:
            config.upper_count = int(sys.argv[1])
            config.lower_count = int(sys.argv[2])
            config.num_count = int(sys.argv[3])
            config.special_count = int(sys.argv[4])
            config.toggle_hand = bool(int(sys.argv[5]))
            config.allow_doubles = bool(int(sys.argv[6]))
            config.human = bool(int(sys.argv[7]))

    except IndexError, ValueError:
        pass
    sys.stderr.write('{0}\n'.format(config))
    password = password_generator.generate_password(config)
    print password

if __name__ == '__main__': main()
