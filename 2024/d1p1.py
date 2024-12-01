import sys


def main(text: str):
    arr1 = []
    arr2 = []

    for line in text.splitlines():
        x, y = line.split()

        arr1.append(int(x))
        arr2.append(int(y))

    arr1.sort()
    arr2.sort()

    return sum([abs(x - y) for (x, y) in zip(arr1, arr2)])


def test():
    input = "3   4\n4   3\n2   5\n1   3\n3   9\n3   3"
    assert 11 == main(input)


if __name__ == "__main__":
    text = ""

    if not sys.stdin.isatty():
        text = sys.stdin.read()
    elif len(sys.argv) > 1:
        text = sys.argv[1]

    print(main(text)) if text != "" else test()

    sys.exit(0)
