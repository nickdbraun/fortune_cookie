def get_initials(fullname):
    """ Given a person's name, returns the person's initials (uppercase) """
    # TODO your code her
    name=fullname.split()
    initials =(letter [0].upper() for letter in name)
    initials = ''.join(initials)
    return initials
def main():
    fullname =input("What is your full name?")
    print(get_initials(fullname))
if __name__ == '__main__':
    main()
