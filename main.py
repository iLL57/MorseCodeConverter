from morse_key import morse_key


def encode(text):
    encod_msg = []
    for char in text.upper():
        if char in morse_key:
            encod_msg.append(morse_key[char])
        else:
            raise ValueError(f"Sorry, {char} is cannot be converted into Morse Code at this time.")
    return ' '.join(encod_msg)


def decode(morse_code):
    letter_key = {value: key for key, value in morse_key.items()}
    decode_msg = []
    for code in morse_code.split(' '):
        if code in letter_key:
            decode_msg.append(letter_key[code])
        elif code == '/':
            decode_msg.append(' ')
        else:
            raise ValueError(f"Sorry, {code} was not able to be decoded. Please try again.")
    return ''.join(decode_msg).title()


# cont_encrypt = True

# while cont_encrypt:
#     code_decode = input('Type "1" to encrypt or "2" to decode.\n')
#     user_msg = input("Enter your message: \n")
#     if code_decode == '1':
#         try:
#             encoded_msg = encode(user_msg.upper())
#             print(f"Encoded message: {encoded_msg}\n")
#         except ValueError as e:
#             print(e)
#     elif code_decode == '2':
#         try:
#             decoded_msg = decode(user_msg)
#             print(f"Decoded message: {decoded_msg}\n")
#         except ValueError as e:
#             print(e)
#     else:
#         print("Invalid input. Please enter '1' to encrypt or '2' to decode.\n")
#
#     continue_code = input('Would you like to encrypt or decode another message? (Y/N)\n')
#     if continue_code.upper() == 'N':
#         print('Thank you for using!')
#         cont_encrypt = False
