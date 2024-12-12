import sys


def main(text: str) -> int:
    A = [[int(char) for char in line] for line in text.splitlines()]
    m, n = len(A), len(A[0])

    def count_trails(x: int, y: int) -> int:
        nonlocal A, m, n

        z = 0

        if A[x][y] == 9:
            z += 1
        else:
            if x > 0 and A[x-1][y] == A[x][y] + 1:
                z += count_trails(x-1, y)
            if y > 0 and A[x][y-1] == A[x][y] + 1:
                z += count_trails(x, y-1)
            if x < m - 1 and A[x+1][y] == A[x][y] + 1:
                z += count_trails(x+1, y)
            if y < n - 1 and A[x][y+1] == A[x][y] + 1:
                z += count_trails(x, y+1)

        return z

    b = 0

    for i in range(m):
        for j in range(n):
            if A[i][j] == 0:
                b += count_trails(i, j)

    return b


def test():
    input = "89010123\n78121874\n87430965\n96549874\n45678903\n32019012\n01329801\n10456732"
    assert 81 == main(input)


if __name__ == "__main__":
    text = ""

    if not sys.stdin.isatty():
        text = sys.stdin.read()
    elif len(sys.argv) > 1:
        text = sys.argv[1]

    print(main(text)) if text != "" else test()

    sys.exit(0)
