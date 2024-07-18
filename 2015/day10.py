#!/usr/bin/env python

import sys


def challenge(number: str) -> str:
    def look_and_say(number: str) -> str:
        crr_digit = number[0]
        crr_digit_count = 0
        result = ""

        for digit in number:
            if digit != crr_digit:
                result += f"{crr_digit_count}{crr_digit}"
                crr_digit = digit
                crr_digit_count = 1
            else:
                crr_digit_count += 1

        return result + f"{crr_digit_count}{crr_digit}"

    n = number

    for _ in range(50):
        n = look_and_say(n)

    return len(n)


if __name__ == "__main__":
    number = ""

    if not sys.stdin.isatty():
        number = sys.stdin.read()
    else:
        number = sys.argv[1]

    print(challenge(number))
