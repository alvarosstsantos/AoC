import sys


def main(text: str) -> int:
    y = 0

    for line in text.splitlines():
        X = [int(x) for x in line.split()]
        b = 1 if X[0] > X[1] else -1
        y += 1

        for i in range(1, len(X)):
            d = (X[i-1] - X[i]) * b

            if (d < 1 or d > 3):
                y -= 1
                break

    return y


def test():
    input = "7 6 4 2 1\n1 2 7 8 9\n9 7 6 2 1\n1 3 2 4 5\n8 6 4 4 1\n1 3 6 7 9"
    assert 2 == main(input)


if __name__ == "__main__":
    text = ""

    if not sys.stdin.isatty():
        text = sys.stdin.read()
    elif len(sys.argv) > 1:
        text = sys.argv[1]

    print(main(text)) if text != "" else test()

    sys.exit(0)
