import sys
from typing import Set, Tuple


def main(text: str) -> int:
    A = [[int(char) for char in line] for line in text.splitlines()]
    m, n = len(A), len(A[0])

    def follow_trails(x: int, y: int, z: Set[Tuple[int, int]]) -> Set[Tuple[int, int]]:
        nonlocal A, m, n

        if A[x][y] == 9:
            z.update({(x, y)})
        else:
            if x > 0 and A[x-1][y] == A[x][y] + 1:
                z.update(follow_trails(x-1, y, z))
            if y > 0 and A[x][y-1] == A[x][y] + 1:
                z.update(follow_trails(x, y-1, z))
            if x < m - 1 and A[x+1][y] == A[x][y] + 1:
                z.update(follow_trails(x+1, y, z))
            if y < n - 1 and A[x][y+1] == A[x][y] + 1:
                z.update(follow_trails(x, y+1, z))

        return z

    b = 0

    for i in range(m):
        for j in range(n):
            if A[i][j] == 0:
                b += len(follow_trails(i, j, {*()}))

    return b


def test():
    input = "89010123\n78121874\n87430965\n96549874\n45678903\n32019012\n01329801\n10456732"
    assert 36 == main(input)


if __name__ == "__main__":
    text = ""

    if not sys.stdin.isatty():
        text = sys.stdin.read()
    elif len(sys.argv) > 1:
        text = sys.argv[1]

    print(main(text)) if text != "" else test()

    sys.exit(0)
