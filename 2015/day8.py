#!/usr/bin/env python

import sys
import re


def challenge(strings: str) -> int:
    representation = 0
    # memory = 0
    encoded = 0

    for string in strings.split("\n"):
        representation += len(string)
        encoded += len(string) + 2 + len(re.findall(r"\\|\"", string))

        # i = 0
        # encoded += 2

        # while i < len(string):
        #     if string[i] == "\"":
        #         representation += 1
        #         encoded += 2
        #         i += 1

        #     elif string[i] == "\\":
        #         if string[i+1] == "\\" or string[i+1] == "\"":
        #             representation += 2
        #             encoded += 4
        #             memory += 1
        #             i += 2
        #         elif string[i+1] == "x":
        #             representation += 4
        #             encoded += 5
        #             memory += 1
        #             i += 4
        #     else:
        #         representation += 1
        #         encoded += 1
        #         memory += 1
        #         i += 1

    return encoded - representation


if __name__ == "__main__":
    text = ""

    if not sys.stdin.isatty():
        text = sys.stdin.read()
    else:
        text = sys.argv[1]

    print(challenge(text))
