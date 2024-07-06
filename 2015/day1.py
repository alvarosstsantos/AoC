import sys
from functools import reduce


def challenge_1(instructions: str = sys.argv[1]):
    return reduce(lambda x, y: x + 1 if y == "(" else x - 1, instructions, 0)


def challenge_2(instructions: str = sys.argv[1]):
    floor = 0

    for i,  x in enumerate(instructions, start=1):
        floor += (x == "(") - (x == ")")

        if floor < 0:
            return i
