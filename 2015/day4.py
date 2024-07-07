import sys
import hashlib


def challenge_12(secret: str = sys.argv[1]):
    # sys.maxsize returns largest computable tail
    tail = 0

    while (True):
        hash = hashlib.md5(f"{secret}{tail}".encode('utf-8')).hexdigest()

        if (hash.startswith("0" * 5)):
            return tail

        tail += 1


print(challenge_12())
