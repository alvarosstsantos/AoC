import sys
from typing import List


def main(text: str) -> int:
    def g(Y: List[int], x: int, target: int) -> List[int]:
        Z = []

        for y in Y:
            W = [y + x, y * x, int(str(y) + str(x))]

            for w in W:
                if w <= target:
                    Z.append(w)

        return Z

    def f(X: List[int], target: int) -> bool:
        Y = [X[0]]

        for x in X[1:]:
            Y = g(Y, x, target)

        return target in Y

    s = 0

    for line in text.splitlines():
        a, b = line.split(":")
        y = int(a)
        X = [int(x) for x in b.split()]

        if f(X, y):
            s += y

    return s


def test():
    input = "190: 10 19\n3267: 81 40 27\n83: 17 5\n156: 15 6\n7290: 6 8 6 15\n161011: 16 10 13\n192: 17 8 14\n21037: 9 7 18 13\n292: 11 6 16 20"
    assert 11387 == main(input)


if __name__ == "__main__":
    text = ""

    if not sys.stdin.isatty():
        text = sys.stdin.read()
    elif len(sys.argv) > 1:
        text = sys.argv[1]

    print(main(text)) if text != "" else test()

    sys.exit(0)
