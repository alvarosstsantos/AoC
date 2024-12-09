import sys
from typing import List


def main(text: str) -> int:
    def descompact(text: str) -> List[int]:
        X = []

        for i in range(len(text)):
            if i % 2 == 0:
                X.extend([i // 2] * int(text[i]))
            else:
                X.extend([None] * int(text[i]))

        return X

    def checksum(X: List[int]) -> int:
        y = 0

        for i in range(len(X)):
            y += i * X[i] if X[i] is not None else 0

        return y

    def find_block_start(X: List[int], i) -> int:
        id = X[i]

        while True:
            if (i > 0 and X[i - 1] == id):
                i -= 1
            else:
                break

        return i

    def find_fitting_free_space_start(X: List[int], i, block_size) -> int:
        for j in range(i):
            fit = True

            for k in range(j, j + block_size):
                if X[k] is not None:
                    fit = False
                    break

            if fit:
                return j

        return -1

    X = descompact(text)

    i = len(X) - 1

    while i > 0:
        if X[i] is None:
            i -= 1
            continue

        j = find_block_start(X, i)

        block_size = 1 + i - j

        k = find_fitting_free_space_start(X, j, block_size)

        if k > -1:
            for m in range(block_size):
                X[k + m] = X[i - m]
                X[i - m] = None

        i -= block_size

    return checksum(X)


def test():
    input = "2333133121414131402"
    assert 2858 == main(input)


if __name__ == "__main__":
    text = ""

    if not sys.stdin.isatty():
        text = sys.stdin.read()
    elif len(sys.argv) > 1:
        text = sys.argv[1]

    print(main(text)) if text != "" else test()

    sys.exit(0)
