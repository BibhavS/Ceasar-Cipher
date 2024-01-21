def welcome():
    print("Welcome to the Caesar Cipher")
    print("This program encrypts and decrypts text with the Caesar Cipher.")
    print()


def enter_message():
    flag = True
    while flag:
        mode = input("Would you like to encrypt (e) or decrypt (d)? ").lower()
        if mode == 'e' or mode == 'd':
            flag = False
        else:
            print("Invalid Mode")

    while True:
        message = input("What message would you like to {}? ".format("encrypt" if mode == 'e' else "decrypt"))
        shift_str = input("What is the shift number: ")

        try:
            shift = int(shift_str)
            break
        except ValueError:
            print("Invalid Shift")

    return mode, message.upper(), shift


def encrypt(message, shift):
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            shifted_char = chr((ord(char) - ord('A' if char.isupper() else 'a') + shift) % 26 + ord('A'))
            encrypted_message += shifted_char
        else:
            encrypted_message += char

    return encrypted_message


def decrypt(message, shift):
    return encrypt(message, -shift)


def is_file(filename):
    try:
        with open(filename, 'r'):
            pass
        return True
    except FileNotFoundError:
        return False


def write_messages(messages):
    with open('results.txt', 'w') as file:
        for message in messages:
            file.write(message + '\n')


def process_file(filename, mode, shift):
    messages = []
    with open(filename, 'r') as file:
        for line in file:
            message = line.strip()
            if mode == 'e':
                messages.append(encrypt(message, shift))
            elif mode == 'd':
                messages.append(decrypt(message, shift))
    return messages


def message_or_file():
    while True:
        mode = input("Would you like to encrypt (e) or decrypt (d)? ").lower()
        if mode in ('e', 'd'):
            break
        else:
            print("Invalid Mode")

    while True:
        input_type = input("Would you like to read from a file (f) or the console (c)? ").lower()
        if input_type in ('f', 'c'):
            break
        else:
            print("Invalid Input Type")

    message = ''
    filename = ''
    if input_type == 'c':
        message = input("What message would you like to {}? ".format("encrypt" if mode == 'e' else "decrypt"))
    else:
        while True:
            filename = input("Enter a filename: ")
            if is_file(filename):
                break
            else:
                print("Invalid Filename")

    shift_str = input("What is the shift number: ")

    try:
        shift = int(shift_str)
    except ValueError:
        print("Invalid Shift")

    return mode, message.upper(), filename, shift


def main():
    welcome()

    flag = True

    while flag:
        mode, message, filename, shift = message_or_file()

        if filename:
            messages = process_file(filename, mode, shift)
            write_messages(messages)
            print("Output written to results.txt")
        else:
            result = encrypt(message, shift) if mode == 'e' else decrypt(message, shift)
            print(result)

        while True:
            another_message = input("Would you like to encrypt or decrypt another message? (y/n): ").lower()

            if another_message == 'y':
                break

            elif another_message == 'n':
                print("Thank you for using the program")
                flag = False
                break

            else:
                print("Invalid input") 


if __name__ == "__main__":
    main()