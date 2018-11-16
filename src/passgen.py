#!/usr/bin/env python3

import argparse
import sys

import password_generator

from password_config import PasswordConfig

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('difficulty', default=None)
    parser.add_argument('--upper', type=int, default=None)
    parser.add_argument('--lower', type=int, default=None)
    parser.add_argument('--special', type=int, default=None)
    parser.add_argument('--toggle', action='store_true')
    parser.add_argument('--duplicates', action='store_true')
    return parser.parse_args()

def main():
    if len(sys.argv) > 1:
        args = parse_args()
        config = PasswordConfig(difficulty=args.difficulty,
                                upper_count=args.upper,
                                lower_count=args.lower,
                                special_count=args.special,
                                toggle_hand=args.toggle,
                                allow_doubles=args.duplicates)
    else:
        config = PasswordConfig()
    sys.stderr.write('{}\n'.format(config))
    password = password_generator.generate_password(config)
    print(password)

if __name__ == '__main__':
    main()
