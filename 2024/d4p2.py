import sys
from typing import List


def main(text: str) -> int:
    X = []

    for line in text.splitlines():
        character = []

        for char in line:
            character.append(char)
        X.append(character)

    y, m, n = 0, len(X), len(X[0]) if X else 0
    cross = {"SM", "MS"}

    def K(a, b) -> List[str]:
        return X[a-1][b-1] + X[a+1][b+1]

    def L(a, b) -> List[str]:
        return X[a+1][b-1] + X[a-1][b+1]

    for i in range(1, m-1):
        for j in range(1, n-1):
            if X[i][j] == "A" and K(i, j) in cross and L(i, j) in cross:
                y += 1

    return y


def test():
    input = ".M.S......\n..A..MSMS.\n.M.S.MAA..\n..A.ASMSM.\n.M.S.M....\n..........\nS.S.S.S.S.\n.A.A.A.A..\nM.M.M.M.M.\n.........."
    assert 9 == main(input)


if __name__ == "__main__":
    text = ""

    if not sys.stdin.isatty():
        text = sys.stdin.read()
    elif len(sys.argv) > 1:
        text = sys.argv[1]

    print(main(text)) if text != "" else test()

    sys.exit(0)
