#!/usr/bin/env python

import sys

moves = {
    ">": (1, 0),
    "<": (-1, 0),
    "^": (0, 1),
    "v": (0, -1)
}


def challenge_1(directions: str) -> int:
    x = y = 0
    visited = {(x, y)}

    for direction in directions:
        dx, dy = moves.get(direction, (0, 0))
        x += dx
        y += dy
        visited.add((x, y))

    return len(visited)


def challenge_2(directions: str) -> int:
    x = [0, 0]
    y = [0, 0]

    visited = {(x[0], y[0])}

    for idx, direction in enumerate(directions):
        dx, dy = moves.get(direction, (0, 0))

        driver = idx % 2

        x[driver] += dx
        y[driver] += dy

        visited.add((x[driver], y[driver]))

    return len(visited)


if __name__ == "__main__":
    directions = ""

    if not sys.stdin.isatty():
        directions = sys.stdin.read()
    else:
        directions = sys.argv[1]

    print(challenge_2(directions))
