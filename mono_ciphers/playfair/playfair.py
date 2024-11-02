import os
import string
import numpy as np
import utils


def generate_key(key: str) -> np.array:
    """
    Generates a 5x5 key matrix for the Playfair cipher from a given keyword.
    Removes duplicate characters from the keyword, removes 'J', and fills the matrix with remaining letters.

    Args:
        key (str): The keyword used to generate the key matrix. Duplicates and the letter 'J' are ignored.

    Returns:
        np.array: A 5x5 numpy array representing the Playfair cipher key matrix.
    """
    input_key = str.upper(key)

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


def process(base_dir: str, mode: bool) -> None:
    """
    Processes either encryption or decryption for a series of keys read from a file.

    Args:
        base_dir (str): The starting dir of reference.
        mode (bool): The mode of operation. `0` for encrypt, `1` for decrypt.
    """
    keys = utils.get_keys(base_dir)

    if mode == 0:
        plaintext = utils.get_text(base_dir, "plaintext.txt", 0)

        for i, key in enumerate(keys):
            key = generate_key(key)

            result_text = process_text(plaintext, key, 0)

            utils.save_result(base_dir, i, result_text, 0)
    else:
        for i, key in enumerate(keys):
            input_filename = f"cipher_{i + 1:02}.txt"

            key = generate_key(key)

            ciphertext = utils.get_text(base_dir, input_filename, 1)

            result_text = process_text(ciphertext, key, 1)

            utils.save_result(base_dir, i, result_text, 1)


def find_axis(i: str, j: str, key: np.array, mode: bool) -> list[str]:
    """
    This function finds the positions of the input characters in the key matrix.
    If the characters are in the same row, it shifts horizontally.
    If in the same column, it shifts vertically.
    If the characters form a rectangle, it swaps their columns.
    The shift direction depends on the mode.

    Args:
        i (str): The first character to process.
        j (str): The second character to process.
        key (np.array): A 5x5 numpy array representing the Playfair cipher key matrix.
        mode (bool): The mode of operation; if 0, shifts forward (encryption), if 1, shifts backward (decryption).

    Returns:
        list[str]: A list containing the two resulting characters after applying the Playfair cipher rules.
    """

    i_x, i_y = np.where(key == i)
    j_x, j_y = np.where(key == j)

    i_x, i_y = int(i_x[0]), int(i_y[0])
    j_x, j_y = int(j_x[0]), int(j_y[0])

    if i_x == j_x:
        # same row, horizontal shift
        shift = 1 if mode == 0 else -1

        i_y = (i_y + shift) % 5
        j_y = (j_y + shift) % 5
    elif i_y == j_y:
        # same column, vertical shift
        shift = 1 if mode == 0 else -1

        i_x = (i_x + shift) % 5
        j_x = (j_x + shift) % 5
    else:
        # rectangle, switch column
        i_y, j_y = j_y, i_y

    i_w = key[i_x, i_y]
    j_w = key[j_x, j_y]

    return i_w, j_w


def process_text(text: str, key: np.array, mode: bool) -> str:
    """
    Encrypt or decrypt an input plaintext.
    If there is a dobule-letter word, it would be divided by an "X".

    Args:
        text (str); The plaintext.
        key (int): The Key.
        mode (bool): The mode of operation. `0` for encrypt, `1` for decrypt.

    Returns:
        str: The entire input text processed.
    """
    encrypted_text = ""

    if len(text) % 2 != 0:
        text += "X"

    for idx in range(0, len(text), 2):
        i = text[idx]
        j = text[idx + 1]

        i_w, j_w = find_axis(i, j, key, mode)

        encrypted_text += i_w + j_w

    return encrypted_text


if __name__ == "__main__":
    base_dir = os.path.dirname(__file__)
    utils.ensure_directories(base_dir)

    operation = input("0 Cypher / 1 Decrypt:")

    if operation == "0":
        process(base_dir, 0)
    elif operation == "1":
        # add if no file in cipher, exit
        process(base_dir, 1)
    else:
        print("Invalid operation selected.")
