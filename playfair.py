import numpy as np
import string

# REFACTOR
# create def
# add try except to key input
input_key = str.upper(input("\nInsert the shift value (integer):\n"))
print("key:", input_key)

key = []

uppercase_alphabet = list(string.ascii_uppercase)
uppercase_alphabet.remove("J")

for i in input_key:
    if i not in key:
        key.append(i)
        uppercase_alphabet.remove(i)
        previous_char = i


print(uppercase_alphabet)
print(key)

for letter in uppercase_alphabet:
    (key.append(letter))
print(key)


key_matrix = np.array(list(key)).reshape(5, 5)
print("key_matrix: \n", key_matrix)


input_plaintext = input("\nInsert text: ").upper()
encrypted_text = ""

for idx in range(0, len(input_plaintext), 2):
    i = input_plaintext[idx]
    j = input_plaintext[idx + 1]

    # find axis

    i_x, i_y = np.where(key_matrix == i)
    j_x, j_y = np.where(key_matrix == j)

    i_x, i_y = i_x[0], i_y[0]
    j_x, j_y = j_x[0], j_y[0]

    if i_x == j_x:
        # if same row shift colum
        i_y = (i_y + 1) % 5
        j_y = (j_y + 1) % 5
    elif i_y == j_y:
        # shift row
        i_x = (i_x + 1) % 5
        j_x = (j_x + 1) % 5

    else:
        # colum switch
        i_y, j_y = j_y, i_y

    i_w = key_matrix[i_x, i_y]
    j_w = key_matrix[j_x, j_y]

    encrypted_text += i_w + j_w

print(encrypted_text)
