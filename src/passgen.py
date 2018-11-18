#!/usr/bin/env python3

import argparse
import sys

import password_generator

from password_config import PasswordConfig

allowed_difficulties = ['easy', 'medium', 'hard', 'insane']

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('difficulty', nargs='?', default=None)
    parser.add_argument('--upper', type=int, default=None)
    parser.add_argument('--lower', type=int, default=None)
    parser.add_argument('--num', type=int, default=None)
    parser.add_argument('--special', type=int, default=None)
    parser.add_argument('--toggle', action='store_true')
    parser.add_argument('--duplicates', action='store_true')
    return parser.parse_args()

def main():
    args = parse_args()
    if args.difficulty == None and len(sys.argv) == 1:
        args.difficulty = 'medium'
    config = PasswordConfig(difficulty=args.difficulty,
                            upper_count=args.upper,
                            lower_count=args.lower,
                            num_count=args.num,
                            special_count=args.special,
                            toggle_hand=args.toggle,
                            allow_doubles=args.duplicates)
    sys.stderr.write('{}\n'.format(config))
    password = password_generator.generate_password(config)
    print(password)

if __name__ == '__main__':
    main()
