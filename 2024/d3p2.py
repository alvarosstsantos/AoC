import re
import sys


def main(text: str) -> int:
    p = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")
    y = 0
    i = 0

    while i < len(text) - 7:
        if text[i:i+7] == "don't()":
            j = text[i+6:].find("do()")

            if j > -1:
                i += j + 4
                continue
            break

        m = re.search(p, text[i:i+12])

        if m:
            y += int(m.group(1)) * int(m.group(2))
            i += m.end()
        else:
            i += 1

    return y


def test():
    input = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    assert 48 == main(input)


if __name__ == "__main__":
    text = ""

    if not sys.stdin.isatty():
        text = sys.stdin.read()
    elif len(sys.argv) > 1:
        text = sys.argv[1]

    print(main(text)) if text != "" else test()

    sys.exit(0)
