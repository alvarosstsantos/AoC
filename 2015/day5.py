#!/usr/bin/env python

import sys


def challenge_1(text: str) -> int:
    vowels = 'aeiou'
    forbidden = ['ab', 'cd', 'pq', 'xy']

    nice = 0

    for string in text.split():
        vowel_count = 1 if string[0] in vowels else 0
        repeat_count = 0
        contain_forbbiden = False

        for i in range(1, len(string)):
            if string[i-1:i+1] in forbidden:
                contain_forbbiden = True
                continue

            if string[i] in vowels:
                vowel_count += 1

            if string[i] == string[i-1]:
                repeat_count += 1

        if not contain_forbbiden and vowel_count >= 3 and repeat_count >= 1:
            nice += 1

    return nice


def challenge_2(text: str) -> int:
    nice = 0

    for string in text.split():
        one_character_repeat = False
        two_character_repeat = False

        for i in range(0, len(string) - 2):
            if string[i] == string[i+2]:
                one_character_repeat = True

            if string[i:i+2] in string[i+2:]:
                two_character_repeat = True

            if one_character_repeat and two_character_repeat:
                nice += 1
                break

    return nice


if __name__ == "__main__":
    text = ""

    if not sys.stdin.isatty():
        text = sys.stdin.read()
    else:
        text = sys.argv[1]

    print(challenge_2(text))
