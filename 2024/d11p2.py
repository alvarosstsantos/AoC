import sys
from typing import Dict


def main(text: str) -> int:
    X = {0: (1,)}

    def add(x: int):
        nonlocal X

        if x in X:
            return
        else:
            y = str(x)
            m = len(y)

            if ((m % 2) == 0):
                x1 = int(y[:m // 2])
                x2 = int(y[m // 2:])

                X[x] = (x1, x2)

                add(x1)
                add(x2)
            else:
                x1 = x * 2024

                X[x] = (x1, )

                add(x1)

    def init() -> Dict[int, int]:
        nonlocal X

        Y = {}

        for x in X:
            Y[x] = 0

        return Y

    Z = [int(z) for z in text.strip().split()]

    for z in Z:
        add(z)

    Y = init()

    for z in Z:
        Y[z] = 1

    for _ in range(75):
        W = init()

        for y in Y:
            if Y[y] > 0:
                for x in X[y]:
                    W[x] += Y[y]

        Y = W

    return sum(Y.values())


def test():
    input = "125 17"
    print(main(input))


if __name__ == "__main__":
    text = ""

    if not sys.stdin.isatty():
        text = sys.stdin.read()
    elif len(sys.argv) > 1:
        text = sys.argv[1]

    print(main(text)) if text != "" else test()

    sys.exit(0)
