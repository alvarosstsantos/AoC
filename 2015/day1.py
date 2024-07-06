import sys

instructions: str = sys.argv[1]

floor = 0

for idx, i in enumerate(instructions, start = 1):
    if i == "(":
        floor += 1
    elif i == ")":
        floor -= 1
    else:
        print("Invalid Instruction", i)
        break

    if floor <= -1:
        print(idx)
        break
