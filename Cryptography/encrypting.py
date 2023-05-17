'''
Create an encrypt function which takes two parameters : message and shift number.
Then inside this function shift each letter of the message forwards in the alphabet by the shift number and return encrypted text.
'''

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
            'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


'''
def encrypt(p_message, p_number):
    cipher_message = ''
    for char in p_message:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + p_number
            if new_position > 25:
                new_position -= 26 # Because we have 26 alphabet according to indexing
            new_char = alphabet[new_position]
            cipher_message += new_char
        else:
            cipher_message += char # This will add any element not in alphabet, added to the message to prevent errors
    return f' The real message is {p_message}, and the encoded message is {cipher_message}'


message = input("Enter your message:\n").upper()
shift_number = int(input("Enter the shift number:\n"))
def decrypt(p_message, p_number):
    decipher_message = ''
    for char in p_message:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position - p_number
            if new_position < 0:
                new_position += 26 # Because we have 26 alphabet according to indexing
            new_char = alphabet[new_position]
            decipher_message += new_char
        else:
            decipher_message += char # This will add any element not in alphabet, added to the message to prevent errors
    return f' The encrypted message is {p_message}, and the decrypted message is {decipher_message}'

print(encrypt(message, shift_number))
'''

# Combining
def encrypt(p_message, p_number):
    cipher_message = ''
    for char in p_message:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + p_number
            if new_position > 25:
                new_position -= 26 # Because we have 26 alphabet according to indexing
            new_char = alphabet[new_position]
            cipher_message += new_char
        else:
            cipher_message += char # This will add any element not in alphabet, added to the message to prevent errors
    return f' The real message is {p_message}, and the encoded message is {cipher_message}'



def decrypt(p_message, p_number):
    decipher_message = ''
    for char in p_message:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position - p_number
            if new_position < 0:
                new_position += 26 # Because we have 26 alphabet according to indexing
            new_char = alphabet[new_position]
            decipher_message += new_char
        else:
            decipher_message += char # This will add any element not in alphabet, added to the message to prevent errors
    return f' The encrypted message is {p_message}, and the decrypted message is {decipher_message}'

message = input("Enter your message:\n").upper()
shift_number = int(input("Enter the shift number:\n"))
question = input('Do you want to encrypt or decrypt? ')

if question == 'encrypt':
    print(encrypt(message, shift_number))
elif question == 'decrypt':
    print(decrypt(message, shift_number))
else:
    print('Can\'t perform any operation. Thanks')