#!/usr/bin/env python

import sys


def challenge(instructions: str) -> int:
    graph = {}

    memo = {}

    def evaluate(node):
        if isinstance(node, int):
            return node

        if (node['key'] in memo):
            return memo[node['key']]

        if node['operation'] is None:
            memo[node['key']] = evaluate(node['left'])
            return memo[node['key']]

        left = evaluate(node['left'])
        right = evaluate(node['right']) if node['right'] is not None else None

        value = None

        if node['operation'] == 'AND':
            value = left & right
        elif node['operation'] == 'OR':
            value = left | right
        elif node['operation'] == 'XOR':
            value = left ^ right
        elif node['operation'] == 'RSHIFT':
            value = left >> right
        elif node['operation'] == 'LSHIFT':
            value = left << right
        elif node['operation'] == 'NOT':
            value = left ^ 0xffff
        else:
            raise ValueError(f"Unsupported operation: {node['operation']}")

        memo[node['key']] = value
        return memo[node['key']]

    for instruction in instructions.split("\n"):
        i = instruction.split()

        left, operation, right, node = None, None, None, None

        if len(i) == 3:
            [left, _, node] = i
        elif len(i) == 4:
            [operation, left, _, node] = i
        else:
            [left, operation, right, _, node] = i

        graph[node] = {
            'key': node,
            'left': left,
            'right': right,
            'operation': operation,
        }

    for key in graph:
        node = graph[key]

        if node['left'] is not None:
            if node['left'].isdigit():
                node['left'] = int(node['left'])
            else:
                node['left'] = graph.get(node['left'])

        if node['right'] is not None:
            if node['right'].isdigit():
                node['right'] = int(node['right'])
            else:
                node['right'] = graph.get(node['right'])

    return evaluate(graph['a'])


if __name__ == "__main__":
    text = ""

    if not sys.stdin.isatty():
        text = sys.stdin.read()
    else:
        text = sys.argv[1]

    print(challenge(text))
