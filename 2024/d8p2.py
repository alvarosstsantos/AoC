import sys


def main(text: str) -> int:
    A = [[char for char in line] for line in text.splitlines()]
    m = len(A)
    n = len(A[0])
    B = [[False] * n for _ in range(m)]

    def resonate(x1: int, y1: int) -> None:
        nonlocal A, B
        z = A[x1][y1]

        for i in range(m):
            for j in range(n):
                if i != x1 and j != y1 and A[i][j] == z:
                    dx, dy = x1 - i, y1 - j

                    x2, y2 = x1 + dx, y1 + dy
                    while (0 <= x2 < m) and (0 <= y2 < n):
                        B[x2][y2] = True
                        x2 += dx
                        y2 += dy

                    x2, y2 = x1 - dx, y1 - dy
                    while (0 <= x2 < m) and (0 <= y2 < n):
                        B[x2][y2] = True
                        x2 -= dx
                        y2 -= dy

    for i in range(m):
        for j in range(n):
            if A[i][j] != ".":
                resonate(i, j)

    return sum([sum(b) for b in B])


def test():
    input = "............\n........0...\n.....0......\n.......0....\n....0.......\n......A.....\n............\n............\n........A...\n.........A..\n............\n............"
    assert 34 == main(input)


if __name__ == "__main__":
    text = ""

    if not sys.stdin.isatty():
        text = sys.stdin.read()
    elif len(sys.argv) > 1:
        text = sys.argv[1]

    print(main(text)) if text != "" else test()

    sys.exit(0)
