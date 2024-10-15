# SOLVED: solve double letters - SOLVED"

# solve space between words, space = "W"
# solve double in decryption
# make frequency diagram


def print_alphabet(k: int) -> None:
    print("\n")
    uppercase_alphabet = [chr(i) for i in range(ord("A"), ord("Z") + 1)]
    caesar_alphabet = [
        chr((ord(i) - ord("A") + k) % 26 + ord("A")) for i in uppercase_alphabet
    ]
    # caesar_alphabet = [chr(i) for i in range(ord('D'), ord('X') + 3)] + [chr(i) for i in range(ord('A'), ord('C') + 1)]

    print(uppercase_alphabet)
    print(caesar_alphabet)


# MODE:
# 0 ENCRYPT
# 1 DECRYPT
def encrypt_letter(i: str, k: int, mode: bool) -> str:
    if mode == 0:
        return chr((ord(i) - ord("A") + k) % 26 + ord("A"))
    else:
        return chr((ord(i) - ord("A") - k) % 26 + ord("A"))


# add custom padding char
def process_text(k: int, plaintext: str, mode: bool) -> str:
    print_alphabet(k)

    encrypted_text = []
    previous_char = ""

    # add .isalpha
    for i in plaintext:
        j = encrypt_letter(i.upper(), k, mode)

        if previous_char == j:
            encrypted_text.append("X")
        previous_char = j

        encrypted_text.append(j)

    return "".join(encrypted_text)


def process_from_input(mode: bool) -> None:
    try:
        key = int(input("\nInsert the shift value (integer):\n"))
    except ValueError:
        print("error: The shift value must be an integer.")
        return
    text = input(
        "\nInsert text to " + ("decrypt" if mode == 1 else "encrypt") + ":\n"
    ).upper()

    result_text = process_text(key, text, mode)

    print("\n" + ("Decrypted" if mode == 1 else "Encrypted") + " text:\n" + result_text)


def process_from_file(mode: bool) -> None:
    try:
        if mode == 0:
            file = open("plaintext.txt", "r")
        else:
            file = open("ciphertext.txt", "r")

        key = int(file.readline().strip())
        text = file.read()

        result_text = process_text(key, text, mode)
        print(
            "\n"
            + ("Decrypted" if mode == 1 else "Encrypted")
            + " text:\n"
            + result_text
        )
    except FileNotFoundError:
        print("File not found. Please make sure 'plaintext.txt' exists.")
    except ValueError:
        print(
            "Invalid key. Please make sure the first line of the file contains an integer."
        )
