# Information Systems Security

## Project Description

This repository contains exercises and explanations of ciphers and algorithms studied in the *Information Systems Security* course at DIEEI, University of Catania. The project includes implementations of various encryption algorithms, which will be continuously expanded and improved with the addition of new methods and ciphers.

## Exercises and Input

The exercises in this repository require input consisting of:
- A `plaintext.txt` file in the `input` folder, containing the plaintext to be encrypted or decrypted.
- A `keys.txt` file in the same folder, containing one or more encryption keys, each on a separate line.

**Note**: Some algorithms, such as the Caesar cipher, require each key to be an integer. If a key is invalid, an error will be displayed.

## How to Run the Project

1. Clone the repository:

    ```bash
    git clone git@github.com:Teosche/information-systems-security.git
    ```

2. Navigate to the directory of the algorithm you're interested in:

    ```bash
    cd <algorithm_directory>
    ```

3. Run the desired module:

    ```bash
    python3 -m <cipher_name>.<filename>
    ```

    **Examples:**

    From mono_chipers directory:
    - To run the Caesar cipher: 
      ```bash
      python3 -m caesar.caesar
      ```
    - To run the Playfair cipher:
      ```bash
      python3 -m playfair.playfair
      ```

### Execution Example

To encrypt or decrypt a text:
1. Ensure the `input` directory contains the `plaintext.txt` and `keys.txt` files.
2. If they do not already exist, the `cipher` and `decrypt` directories will be automatically created to store results.
3. Start the desired algorithm. 

## Implemented Ciphers

### Monoalphabetic Ciphers

- **Caesar**: The Caesar cipher shifts each letter in the plaintext by a fixed number of positions in the alphabet, determined by the key. For example, with a key of 3, `A` becomes `D`, `B` becomes `E`, and so on.
  
- **Playfair**: The Playfair cipher uses a 5x5 matrix to encrypt pairs of letters. Each letter pair is substituted based on its position in the matrix. If a pair consists of two identical letters, a separator is inserted.

## Technology Stack

The scripts are written in Python.

## Contributions

The repository is continuously evolving. Contributions for implementing new algorithms or improvements are welcome. Feel free to open a pull request or create an issue to report problems or suggestions.

## License

This project is distributed under the MIT license.