import sys
from functools import reduce

instructions: str = sys.argv[1]


def challenge_1():
    print(reduce(lambda x, y: x + 1 if y == "(" else x - 1, instructions, 0))


def challenge_2():
    floor = 0

    for idx, i in enumerate(instructions, start=1):
        if i == "(":
            floor += 1
        else:
            floor -= 1

        if floor <= -1:
            print(idx)
            break


challenge_1()
