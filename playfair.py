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
