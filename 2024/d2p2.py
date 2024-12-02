import sys


def main(text: str) -> int:
    y = 0

    for line in text.splitlines():
        X = [int(x) for x in line.split()]

        i = find_unsafe_level(X)

        if i == -1 or i == len(X) - 1:
            y += 1
        else:
            i1 = find_unsafe_level(X[:i] + X[i+1:])
            i2 = find_unsafe_level(X[:i-1] + X[i:])
            i3 = find_unsafe_level(X[:i-2] + X[i-1:]) if i > 1 else 0

            if i1 == -1 or i2 == -1 or i3 == -1:
                y += 1

    return y


def find_unsafe_level(X):
    b = 1 if X[0] > X[1] else -1

    for i in range(1, len(X)):
        d = (X[i-1] - X[i]) * b

        if (d < 1 or d > 3):
            return i

    return -1


def test():
    input = "7 6 4 2 1\n1 2 7 8 9\n9 7 6 2 1\n1 3 2 4 5\n8 6 4 4 1\n1 3 6 7 9"
    assert 4 == main(input)


if __name__ == "__main__":
    text = ""

    if not sys.stdin.isatty():
        text = sys.stdin.read()
    elif len(sys.argv) > 1:
        text = sys.argv[1]

    print(main(text)) if text != "" else test()

    sys.exit(0)
