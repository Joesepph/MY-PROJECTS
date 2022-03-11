import string

def encrypt(text, s):
    alpha = string.ascii_uppercase
    alpha_lower = string.ascii_lowercase

    result = ""
    
    for letter in text:
        if letter in alpha:
            letter_index = (alpha.find(letter) + s) % len(alpha)

            result = result + alpha[letter_index]
        elif letter in alpha_lower:
            letter_index = (alpha_lower.find(letter) + s) % len(alpha_lower)

            result = result + alpha_lower[letter_index]
        else:
            result = result + letter
    return result


def decrypt(etext, s):
    alpha = string.ascii_uppercase
    alpha_lower = string.ascii_lowercase

    result = ""

    for letter in etext:
        if letter in alpha:
            letter_index = (alpha.find(letter) - s) % len(alpha)

            result = result + alpha[letter_index]
        elif letter in alpha_lower:
            letter_index = (alpha_lower.find(letter) + s) % len(alpha_lower)

            result = result + alpha_lower[letter_index]
        else:
            result = result + letter
    return result

def brute_force():
    message = input("Encrypted text: ")

    alpha = string.ascii_uppercase
    alpha_lower = string.ascii_lowercase
    
    for key in range(len(alpha)):
        translated = ''

        for symbol in message:
            if symbol in alpha:
                num = alpha.find(symbol)
                num = num - key

                if num < 0:
                    num = num + len(alpha)
                translated = translated + alpha[num]
            elif symbol in alpha_lower:
                num = alpha_lower.find(symbol)
                num = num - key

                if num < 0:
                    num = num + len(alpha_lower)
                translated = translated + alpha_lower[num]
            else:
                translated = translated + symbol
        print('Hacking key #%s: %s' % (key, translated))
    


while True:
    choice = input("Do you want to encrypt, decrypt or brute force the caesar cipher? (e/d/b) ").lower()

    if choice == "e":
        text = input("Plain text: ")
        s = int(input("Shift pattern: "))
        print("Encrypted text: ", encrypt(text, s))
    elif choice == "d":
        etext = input("Encrypted text: ")
        s = int(input("Shift pattern: "))
        print("Decrypted text: ", decrypt(etext, s))
    elif choice == "b":
        brute_force()
    else:
        print("Give a proper value!")

    print("")
    end = input("Do you want to encrypt/decrypt again? (y/n) ").lower()

    if end == "y":
        print("\n")
        continue
    elif end == "n":
        print("\n")
        break
    else:
        print("Give a proper value!")