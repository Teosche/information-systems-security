import os
import sys
from typing import Union


def get_keys(base_dir: str) -> Union[list[str], list[int]]:
    """
    Reads and returns a list of keys from 'keys.txt' located in the 'input' directory.
    Reads each line in 'keys.txt', strips whitespace, and returns a list of keys.
    An error message is displayed if the file is missing or contains invalid data.

    Args:
        base_dir (str): The base directory path for the input files.

    Returns:
        Union[list[str], list[int]]: A list of keys as strings or integers, depending on usage.

    Raises:
        ValueError: If a key in 'keys.txt' is invalid.
        FileNotFoundError: If 'keys.txt' does not exist.
    """
    try:
        keys_filepath = os.path.join(base_dir, "input", "keys.txt")

        with open(keys_filepath, "r") as keys_file:
            keys = [key.strip() for key in keys_file.readlines()]

        if not keys:
            print("Error: No keys found in 'keys.txt'.")
            return

        return keys

    except ValueError:
        print("Invalid key. Please make sure 'keys.txt' contains valid strings.")
    except FileNotFoundError as e:
        print(f"Error: {e}")


def get_text(base_dir: str, input_filename, mode: bool) -> str:
    """
    Reads and processes text from a specified file for encryption or decryption.

    Args:
        base_dir (str): The base directory path for the input files.
        input_filename (str): The name of the file to read.
        mode (bool): The mode of operation. `0` for encrypt, `1` for decrypt.

    Returns:
        str: A string of processed text, converted to uppercase and stripped of non-alphabetical characters.

    Raises:
        FileNotFoundError: If the specified file does not exist in the expected directory.

    """
    folder = "input" if mode == 0 else "cipher"

    text_filepath = os.path.join(base_dir, folder, input_filename)

    if not os.path.exists(text_filepath):
        raise FileNotFoundError(f"File '{text_filepath}' not found.")

    with open(text_filepath, "r") as file:
        text = file.read().strip().upper()
        text = "".join([char for char in text if char.isalpha()])

    return text


def save_result(base_dir: str, i: int, text: str, mode: bool) -> None:
    """
    Saves processed text to an output file in the appropriate directory.

    Args:
        base_dir (str): The base directory path for the output files.
        i (int): The index for numbering output files.
        text (str): The processed text to be saved.
        mode (bool): The mode of operation. `0` for encrypt, `1` for decrypt.
    """
    cipher_name = f"cipher_{i + 1:02}.txt"
    decrypt_name = f"decrypetd_{i + 1:02}.txt"

    folder = "cipher" if mode == 0 else "decrypt"
    output_filename = (
        f"{base_dir}/{folder}/{cipher_name if mode == 0 else decrypt_name}"
    )

    with open(output_filename, "w") as output_file:
        output_file.write(text)

    print(f"Saved: {output_filename}")


def ensure_directories(base_dir: str) -> None:
    """
    Ensures that required directories and files exist, creating necessary folders if missing.

    Args:
        base_dir (str): The base directory path for the project.
    """
    input_dir = os.path.join(base_dir, "input")
    cipher_dir = os.path.join(base_dir, "cipher")
    decrypt_dir = os.path.join(base_dir, "decrypt")

    keys_file = os.path.join(input_dir, "keys.txt")
    plaintext_file = os.path.join(input_dir, "plaintext.txt")

    if not os.path.exists(input_dir):
        print(f"Error: Directory 'input' not found at {input_dir}.")
        sys.exit(1)

    if not os.path.isfile(keys_file) or not os.path.isfile(plaintext_file):
        print(f"Error: Files not found in '{input_dir}'.")
        sys.exit(1)

    os.makedirs(cipher_dir, exist_ok=True)
    os.makedirs(decrypt_dir, exist_ok=True)
