#!/usr/bin/env python

from collections import defaultdict
from functools import cache, wraps
import sys
import re


def freezesetargs(func):
    @wraps(func)
    def wrapped(*args, **kwargs):
        args = (frozenset(arg) if isinstance(
            arg, set) else arg for arg in args)
        kwargs = {k: frozenset(v) if isinstance(
            v, set) else v for k, v in kwargs.items()}
        return func(*args, **kwargs)
    return wrapped


def challenge(text: str) -> int:
    pattern = r"(\w+)\sto\s(\w+)\s=\s(\d+)"

    nodes = set()
    distances = defaultdict(dict)

    for line in text.split("\n"):
        match = re.match(pattern, line)

        n1, n2, d = match.groups()

        distances[n1][n2] = int(d)
        distances[n2][n1] = int(d)

        nodes.update([n1, n2])

    smallest_distance = sys.maxsize

    @freezesetargs
    @cache
    def tsp(start, remaining, distance=0):
        nonlocal smallest_distance

        if not remaining:
            if distance < smallest_distance:
                smallest_distance = distance

        for n in remaining:
            d = distances[start][n]

            if d:
                tsp(n, remaining - {n},  distance + d)

    for n in nodes:
        tsp(n, nodes - {n})

    return smallest_distance


if __name__ == "__main__":
    text = ""

    if not sys.stdin.isatty():
        text = sys.stdin.read()
    else:
        text = sys.argv[1]

    print(challenge(text))
