import sys


def main(text: str) -> int:
    X = []

    for i in range(len(text)):
        if i % 2 == 0:
            X.extend([i // 2] * int(text[i]))
        else:
            X.extend([None] * int(text[i]))

    j = 0

    for i in range(len(X) - 1, -1, -1):
        fragmented = False
        for z in range(j, i):
            if X[z] is None:
                X[z] = X.pop(i)
                j, fragmented = z, True

                break

        if not fragmented:
            break

    while X[-1] is None:
        del X[-1]

    y = 0

    for i in range(len(X)):
        y += i * X[i]

    return y


def test():
    input = "2333133121414131402"
    assert 1928 == main(input)


if __name__ == "__main__":
    text = ""

    if not sys.stdin.isatty():
        text = sys.stdin.read()
    elif len(sys.argv) > 1:
        text = sys.argv[1]

    print(main(text)) if text != "" else test()

    sys.exit(0)
