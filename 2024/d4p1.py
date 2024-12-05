import sys
from typing import List, Tuple


def main(text: str) -> int:
    X = [line.strip() for line in text.splitlines()]
    y, m, n = 0, len(X), len(X[0]) if X else 0
    directions = [(-1, 0), (0, -1), (-1, -1), (-1, +1)]

    def section(a: int, b: int, direction: Tuple[int]) -> List[str]:
        nonlocal X, m, n

        dr, dc = direction
        step = 0
        v = []

        while (step < 4 and 0 <= a < m and 0 <= b < n):
            v.append(X[a][b])
            a += dr
            b += dc
            step += 1

        return v

    for i in range(m):
        for j in range(n):
            for d in directions:
                s = "".join(section(i, j, d))

                if s == "XMAS" or s == "SAMX":
                    y += 1

    return y


def test():
    input = "MMMSXXMASM\nMSAMXMSMSA\nAMXSXMAAMM\nMSAMASMSMX\nXMASAMXAMM\nXXAMMXXAMA\nSMSMSASXSS\nSAXAMASAAA\nMAMMMXMMMM\nMXMXAXMASX"
    assert 18 == main(input)


if __name__ == "__main__":
    text = ""

    if not sys.stdin.isatty():
        text = sys.stdin.read()
    elif len(sys.argv) > 1:
        text = sys.argv[1]

    print(main(text)) if text != "" else test()

    sys.exit(0)
