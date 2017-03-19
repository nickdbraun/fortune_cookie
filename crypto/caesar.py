from helpers import alphabet_position, rotate_character

def encrypt(text, rot):
    newph = ""
    for i in range(len(text)):
        newph = newph + rotate_character(text[i],rot)
    return newph
