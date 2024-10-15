import numpy as np
import string

# REFACTOR
# create def
# add try except to key input
# insert padding character


def generate_key() -> np.array:
    input_key = str.upper(input("\nInsert the key (str):\n"))

    key = []

    uppercase_alphabet = list(string.ascii_uppercase)
    uppercase_alphabet.remove("J")

    for i in input_key:
        if i not in key and i != "J":
            key.append(i)
            uppercase_alphabet.remove(i)

    for letter in uppercase_alphabet:
        key.append(letter)

    key_matrix = np.array(list(key)).reshape(5, 5)
    print("key_matrix: \n", key_matrix)

    return key_matrix


def process_text(plaintext: str, key: np.array) -> str:
    encrypted_text = ""

    # padding function for space, character and doubles, check for create utils file
    plaintext = plaintext.replace(" ", "")
    if len(plaintext) % 2 != 0:
        plaintext += "X"

    for idx in range(0, len(plaintext), 2):
        i = plaintext[idx]
        j = plaintext[idx + 1]

        i_w, j_w = find_axis(i, j, key)

        encrypted_text += i_w + j_w

    return encrypted_text


def find_axis(i: str, j: str, key: np.array):
    i_x, i_y = np.where(key == i)
    j_x, j_y = np.where(key == j)

    i_x, i_y = int(i_x[0]), int(i_y[0])
    j_x, j_y = int(j_x[0]), int(j_y[0])

    if i_x == j_x:
        # same row, shift right
        i_y = (i_y + 1) % 5
        j_y = (j_y + 1) % 5
    elif i_y == j_y:
        # same column, shift bot
        i_x = (i_x + 1) % 5
        j_x = (j_x + 1) % 5
    else:
        # rectangle, switch column
        i_y, j_y = j_y, i_y

    i_w = key[i_x, i_y]
    j_w = key[j_x, j_y]

    return i_w, j_w


def process_from_input() -> None:
    key = generate_key()

    input_plaintext = input("\nInsert text: ").upper()
    result_text = process_text(input_plaintext, key)

    print("Encrypted text: " + result_text)
