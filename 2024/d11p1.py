import sys


class Node:
    def set_next(self, node: "Node"):
        self.next = node

    def set_prev(self, node: "Node"):
        self.prev = node

    def __init__(self, val: str):
        self.val = val
        self.next = None
        self.prev = None

    def __repr__(self) -> str:
        return f"prev: {self.prev.val if self.prev else None}, val: {self.val}, next: {self.next.val if self.next else None}"


class LinkedList:
    def add_to_head(self, node: "Node"):
        node.set_next(self.head)
        self.head = node

    def add_to_tail(self, node: "Node"):
        if self.head is None:
            self.head = node
            return

        last_node = None

        for current_node in self:
            last_node = current_node

        last_node.set_next(node)
        node.set_prev(last_node)

    def __init__(self):
        self.head = None

    def __iter__(self):
        node = self.head

        while node is not None:
            yield node
            node = node.next

    def __repr__(self) -> str:
        nodes = []

        for node in self:
            nodes.append(node.val)

        return " -> ".join(nodes)

    def __len__(self) -> int:
        count = 0

        for _ in self:
            count += 1

        return count


def main(text: str) -> int:
    X = LinkedList()

    for x in text.strip().split():
        X.add_to_tail(Node(x))

    for _ in range(25):
        for x in X:
            if x.val == '0':
                x.val = '1'

                continue

            m = len(x.val)

            if ((m % 2) == 0):
                x1 = Node(x.val[:m // 2])
                x2 = Node(str(int(x.val[m // 2:])))

                x1.set_next(x2)
                x2.set_next(x.next)

                if x.prev is not None:
                    x.prev.set_next(x1)
                else:
                    X.head = x1

                x1.set_prev(x.prev)
                x2.set_prev(x1)

                if x.next is not None:
                    x.next.set_prev(x2)

                continue

            x.val = str(int(x.val) * 2024)

    return len(X)


def test():
    input = "125 17"
    assert 55312 == main(input)


if __name__ == "__main__":
    text = ""

    if not sys.stdin.isatty():
        text = sys.stdin.read()
    elif len(sys.argv) > 1:
        text = sys.argv[1]

    print(main(text)) if text != "" else test()

    sys.exit(0)
