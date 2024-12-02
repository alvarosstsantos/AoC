import sys


def main(text: str) -> int:
    X, Y = [], {}

    for line in text.splitlines():
        x, y = line.split()

        X.append(x)

        if y in Y:
            Y[y] += 1
        else:
            Y[y] = 1

    return sum([int(x) * Y.get(x, 0) for x in X])


def test():
    input = "3   4\n4   3\n2   5\n1   3\n3   9\n3   3"
    assert 31 == main(input)


if __name__ == "__main__":
    text = ""

    if not sys.stdin.isatty():
        text = sys.stdin.read()
    elif len(sys.argv) > 1:
        text = sys.argv[1]

    print(main(text)) if text != "" else test()

    sys.exit(0)
