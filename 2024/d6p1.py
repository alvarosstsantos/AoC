import sys
from typing import Tuple


def main(text: str) -> int:
    grid = [[char for char in line] for line in text.splitlines()]
    moves = {"^": {"s": (-1, 0), "r": ">"},
             ">": {"s": (0, 1), "r": "v"},
             "v": {"s": (1, 0), "r": "<"},
             "<": {"s": (0, -1), "r": "^"}}

    height, length = len(grid), len(grid[0]) if grid else 0

    def get_current_position() -> Tuple[str, int, int]:
        nonlocal height, length, moves

        for i in range(height):
            for j in range(length):
                if grid[i][j] in moves:
                    return grid[i][j], i, j

    visited = [[False] * length for i in range(height)]
    direction, x1, y1 = get_current_position()
    grid[x1][y1] = "."

    while True:
        visited[x1][y1] = True
        dx, dy = moves[direction]["s"]
        x2, y2 = x1 + dx, y1 + dy

        if x2 < 0 or x2 == height or y2 < 0 or y2 == length:
            break

        if grid[x2][y2] != "#":
            x1, y1 = x2, y2
        else:
            direction = moves[direction]["r"]

    return sum([sum(line) for line in visited])


def test():
    input = "....#.....\n.........#\n..........\n..#.......\n.......#..\n..........\n.#..^.....\n........#.\n#.........\n......#..."
    assert 41 == main(input)


if __name__ == "__main__":
    text = ""

    if not sys.stdin.isatty():
        text = sys.stdin.read()
    elif len(sys.argv) > 1:
        text = sys.argv[1]

    print(main(text)) if text != "" else test()

    sys.exit(0)
