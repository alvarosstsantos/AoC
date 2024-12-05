import sys
from typing import Dict, List


def main(text: str) -> int:
    A, B = text.split("\n\n")
    C = {}

    for a in A.splitlines():
        x, y = a.split("|")

        if x in C:
            C[x].append(y)
        else:
            C[x] = [y]

    def ordered(z: List[str], C: Dict[str, List[str]]) -> bool:
        for i in range(len(z)):
            for j in range(i):
                if z[j] in C.get(z[i], []):
                    return False

        return True

    s = 0

    for b in B.splitlines():
        z = b.split(",")

        if ordered(z, C):
            s += int(z[len(z) // 2])

    return s


def test():
    input = "47|53\n97|13\n97|61\n97|47\n75|29\n61|13\n75|53\n29|13\n97|29\n53|29\n61|53\n97|53\n61|29\n47|13\n75|47\n97|75\n47|61\n75|61\n47|29\n75|13\n53|13\n\n75,47,61,53,29\n97,61,53,29,13\n75,29,13\n75,97,47,61,53\n61,13,29\n97,13,75,29,47"
    assert 143 == main(input)


if __name__ == "__main__":
    text = ""

    if not sys.stdin.isatty():
        text = sys.stdin.read()
    elif len(sys.argv) > 1:
        text = sys.argv[1]

    print(main(text)) if text != "" else test()

    sys.exit(0)
