def caesar_cipher_encrypt(plain_text, shift):
    encrypted_text = ""
    for char in plain_text:
        if char.isalpha():
            shifted = ord(char) + shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            encrypted_text += chr(shifted)
        else:
            encrypted_text += char
    return encrypted_text

def caesar_cipher_decrypt(cipher_text, shift):
    decrypted_text = ""
    for char in cipher_text:
        if char.isalpha():
            shifted = ord(char) - shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            decrypted_text += chr(shifted)
        else:
            decrypted_text += char
    return decrypted_text

def main():
    choice = input("Enter 'e' for encryption or 'd' for decryption: ").lower()
    if choice == 'e':
        plain_text = input("Enter the plain text: ")
        shift = int(input("Enter the shift value: "))
        encrypted_text = caesar_cipher_encrypt(plain_text, shift)
        print("Encrypted text:", encrypted_text)
    elif choice == 'd':
        cipher_text = input("Enter the cipher text: ")
        shift = int(input("Enter the shift value: "))
        decrypted_text = caesar_cipher_decrypt(cipher_text, shift)
        print("Decrypted text:", decrypted_text)
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
