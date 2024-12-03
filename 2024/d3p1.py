import re
import sys


def main(text: str) -> int:
    p = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")
    y = 0

    for x in re.finditer(p, text):
        y += int(x.group(1)) * int(x.group(2))

    return y


def test():
    input = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
    assert 161 == main(input)


if __name__ == "__main__":
    text = ""

    if not sys.stdin.isatty():
        text = sys.stdin.read()
    elif len(sys.argv) > 1:
        text = sys.argv[1]

    print(main(text)) if text != "" else test()

    sys.exit(0)
