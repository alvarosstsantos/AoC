#!/usr/bin/env python

import sys
import re


def challenge(text: str) -> int:
    pattern = r"(\w+)\sto\s(\w+)\s=\s(\d+)"
    nodes_set: set[tuple[str, str, int]] = set()
    vertices = []

    for line in text.split("\n"):
        match = re.match(pattern, line)

        vertices.append(match.groups())

        nodes_set.add(match.group(1))
        nodes_set.add(match.group(2))

    nodes = list(nodes_set)
    adjacent_nodes_distances: list[list[None | int]] = [
        [None for _ in range(len(nodes))] for _ in range(len(nodes))]

    for node_1, node_2, distance in vertices:
        node_1_index = nodes.index(node_1)
        node_2_index = nodes.index(node_2)

        adjacent_nodes_distances[node_1_index][node_2_index] = int(distance)
        adjacent_nodes_distances[node_2_index][node_1_index] = int(distance)

    def remove_by_index(ls: list, i: int):
        return [e for j, e in enumerate(ls) if j != i]

    smallest_distance = sys.maxsize

    def traverse(node: int, foward_nodes: list[int], total_distance=0):
        nonlocal smallest_distance

        if total_distance is None:
            return None

        if len(foward_nodes) == 0:
            if total_distance < smallest_distance:
                smallest_distance = total_distance

            return total_distance

        for i in range(len(foward_nodes)):
            distance = adjacent_nodes_distances[node][foward_nodes[i]]
            new_total_distance = total_distance + distance if distance is not None else None

            traverse(foward_nodes[i], remove_by_index(
                foward_nodes, i), new_total_distance)

    encoded_nodes = range(len(nodes))

    for n in encoded_nodes:
        traverse(n, remove_by_index(encoded_nodes, n))

    print(smallest_distance)


if __name__ == "__main__":
    text = ""

    if not sys.stdin.isatty():
        text = sys.stdin.read()
    else:
        text = sys.argv[1]

    print(challenge(text))
