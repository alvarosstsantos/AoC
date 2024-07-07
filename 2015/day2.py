import sys


def challenge_1(dimensions: str) -> int:
    d = sorted(map(int, dimensions.split("x")))

    return 3 * d[0] * d[1] + 2 * d[0] * d[2] + 2 * d[1] * d[2]


def challenge_2(dimensions: str) -> int:
    d = sorted(map(int, dimensions.split("x")))

    return d[0] * d[1] * d[2] + 2 * d[0] + 2 * d[1]


total = sum(challenge_1(present) for present in sys.argv[1].split())

print(total)
