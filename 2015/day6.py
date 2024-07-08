#!/usr/bin/env python

import sys
import re


def challenge_1_2(instructions: str) -> int:
    grid = [[0 for _ in range(1000)] for _ in range(1000)]
    pattern = r"(.+)\s(\d+),(\d+)\sthrough\s(\d+),(\d+)"

    for instruction in instructions.split("\n"):
        match = re.search(pattern, instruction)

        action = match.group(1)

        xi, yi = int(match.group(2)), int(match.group(3))
        xe, ye = int(match.group(4)), int(match.group(5))

        for i in range(xi, xe+1):
            for j in range(yi, ye+1):
                if (action == "turn on"):
                    grid[i][j] += 1
                elif (action == "turn off"):
                    grid[i][j] = max(0, grid[i][j] - 1)
                else:
                    grid[i][j] += 2

    return sum([sum(g) for g in grid])


if __name__ == "__main__":
    text = ""

    if not sys.stdin.isatty():
        text = sys.stdin.read()
    else:
        text = sys.argv[1]

    print(challenge_1_2(text))
