def alphabet_position(letter):
    return ord(letter.lower()) - 97

def rotate_character(letter, rot):
    if ord(letter) >= 65 and ord(letter) <= 90:
        newchar = ord(letter) + rot
        if newchar > 90:
            newchar = (newchar % 90) + 64
        return chr(newchar)
    elif ord(letter) >= 97 and ord(letter) <= 122:
        newchar = ord(letter) + rot
        if newchar > 122:
            newchar = (newchar % 122) + 96
        return chr(newchar)
    else:
        return letter

def encrypt(text, rot):
    newph = ""
    for i in range(len(text)):
        newph = newph + rotate_character(text[i],rot)
    return newph
