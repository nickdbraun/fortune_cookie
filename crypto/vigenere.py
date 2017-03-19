from helpers import alphabet_position, rotate_character

def encrypt(message,key):
    mess_counter = 0
    key_counter = 0
    newmessage = ""
    for i in range(len(message)):
        mess_char = message[i]
        if mess_char.isalpha() == True:
            key_char= key[key_counter]
            encrypt_char = rotate_character(mess_char,alphabet_position(key_char))
            key_counter += 1
            if key_counter > len(key)-1:
                key_counter = 0
        else:
            encrypt_char = mess_char
        newmessage = newmessage + encrypt_char
    return newmessage
