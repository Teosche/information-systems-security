import os
import utils


def print_alphabet(key: int) -> None:
    """
    Prints the uppercase alphabet alongside the Caesar-shifted alphabet based on the provided key.

    Args:
        key (int): The shift value for the Caesar cipher.
    """
    print("\n")
    uppercase_alphabet = [chr(i) for i in range(ord("A"), ord("Z") + 1)]
    caesar_alphabet = [
        chr((ord(i) - ord("A") + key) % 26 + ord("A")) for i in uppercase_alphabet
    ]

    print(uppercase_alphabet)
    print(caesar_alphabet)


def process_char(i: str, key: int, mode: bool) -> str:
    """
    Shift the input value according to the key.

    Args:
        i (str): The character to be shifted.
        key (int): The Key.
        mode (bool): The mode of operation. `0` for encrypt, `1` for decrypt.

    Returns:
        str: Ciphered character
    """
    if mode == 0:
        return chr((ord(i) - ord("A") + key) % 26 + ord("A"))
    else:
        return chr((ord(i) - ord("A") - key) % 26 + ord("A"))


def process_text(text: str, key: int, mode: bool) -> str:
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
    print_alphabet(key)

    text = []
    previous_char = ""

    for i in text:
        j = process_char(i.upper(), key, mode)

        if previous_char == j:
            text.append("X")
        previous_char = j

        text.append(j)

    return "".join(text)


def process(base_dir: str, mode: bool) -> None:
    """
    Processes either encryption or decryption for a series of keys read from a file.

    Args:
        base_dir (str): The starting dir of reference.
        mode (bool): The mode of operation. `0` for encrypt, `1` for decrypt.
    """
    keys = utils.get_keys(base_dir)

    keys = [int(key) for key in keys]

    if mode == 0:
        plaintext = utils.get_text(base_dir, "plaintext.txt", 0)

        for i, key in enumerate(keys):

            result_text = process_text(plaintext, key, 0)

            utils.save_result(base_dir, i, result_text, 0)
    else:
        for i, key in enumerate(keys):
            input_filename = f"cipher_{i + 1:02}.txt"

            ciphertext = utils.get_text(base_dir, input_filename, 1)

            result_text = process_text(ciphertext, key, 1)

            utils.save_result(base_dir, i, result_text, 1)


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
