#! /usr/bin/python

import sys

import password_generator

from password_config import PasswordConfig

def main():
    config = PasswordConfig()
    try:
        config.upper_count = int(sys.argv[1])
        config.lower_count = int(sys.argv[2])
        config.num_count = int(sys.argv[3])
        config.special_count = int(sys.argv[4])
        config.toggle_hand = bool(int(sys.argv[5]))
        config.allow_doubles = bool(int(sys.argv[6]))
    except IndexError, ValueError:
        pass
    sys.stderr.write('{0}\n'.format(config))
    password = password_generator.generate_password(config)
    print password

if __name__ == '__main__': main()
