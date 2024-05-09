import art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def caesarcipher(user_action, text, shift):
    len_text = len(text)
    cipher_text = ""
    decipher_text = ""

    if user_action == "encode":
        for char in text:
            if char in alphabet:
                x = alphabet.index(char)
                cipher_text += (alphabet[x + shift])
            else:
                cipher_text += char
        print(cipher_text)

    elif user_action == "decode":
        for char in text:
            if char in alphabet:
                x = alphabet.index(char)
                decipher_text += (alphabet[x - shift])
            else:
                decipher_text += char
        print(decipher_text)


print(art.logo)
keep = False
while not keep:
    user_action = input(print("Type 'encode' to encrypt and 'decode' to decrypt:\n"))
    text = input(print("Type your message:\n")).lower()
    shift = int(input(print("Type the shift number:\n")))
    shift = shift % 26
    caesarcipher(user_action, text, shift)
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        keep = True
        print("Goodbye")