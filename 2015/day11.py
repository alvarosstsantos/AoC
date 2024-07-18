import sys


def find_next_password(current_password: str) -> str:
    min_character_code = 97
    max_character_code = 122

    def increment(password: list[int]) -> list[int]:
        for i in reversed(range(len(password))):
            password[i] += 1

            if (password[i] > max_character_code):
                password[i] = min_character_code
            else:
                return password

    encoded_password = [ord(ch) for ch in current_password]

    is_invalid = True

    while is_invalid:
        encoded_password = increment(encoded_password)

        # check if password contains the characters i, l or o
        if any(ch in encoded_password for ch in [105, 108, 111]):
            continue

        # checks for two non overlapping pairs
        i = 0
        pair_ocurrence = 0

        while i < len(encoded_password) - 1:
            if encoded_password[i] == encoded_password[i + 1]:
                i += 1
                pair_ocurrence += 1

            i += 1

        if pair_ocurrence < 2:
            continue

        # check sequence of three consecutive characters
        for i in range(len(encoded_password) - 2):
            if (encoded_password[i] + 1 == encoded_password[i + 1] and
                    encoded_password[i] + 2 == encoded_password[i + 2]):
                is_invalid = False

    return "".join([chr(ch) for ch in encoded_password])


print(find_next_password(sys.argv[1]))
