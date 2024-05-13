def rail_fence_encrypt(plain_text, key):
    # Create the rail fence pattern
    fence = [['\n' for _ in range(len(plain_text))] for _ in range(key)]
    rail = 0
    direction = False
    for char in plain_text:
        fence[rail][fence[rail].index('\n')] = char
        if rail == 0 or rail == key - 1:
            direction = not direction
        if direction:
            rail += 1
        else:
            rail -= 1
    # Combine the rails into a single string (column-major transformation)
    encrypted_text = ''.join([char for rail in fence for char in rail if char != '\n'])
    return encrypted_text


def rail_fence_decrypt(cipher_text, key):
    # Create the rail fence pattern
    fence = [['\n' for _ in range(len(cipher_text))] for _ in range(key)]
    rail = 0
    direction = False
    # Fill in the fence with placeholder characters
    for i in range(len(cipher_text)):
        fence[rail][i] = '*'
        if rail == 0 or rail == key - 1:
            direction = not direction
        if direction:
            rail += 1
        else:
            rail -= 1
    # Place the characters of the ciphertext on the fence
    index = 0
    for i in range(key):
        for j in range(len(cipher_text)):
            if (fence[i][j] == '*') and (index < len(cipher_text)):
                fence[i][j] = cipher_text[index]
                index += 1
    # Reconstruct the plaintext (column-major transformation)
    rail = 0
    direction = False
    decrypted_text = ''
    for j in range(len(cipher_text)):
        decrypted_text += fence[rail][j]
        if rail == 0 or rail == key - 1:
            direction = not direction
        if direction:
            rail += 1
        else:
            rail -= 1
    return decrypted_text


def main():
    plain_text = input("Enter the plain text: ")
    key = int(input("Enter the key (number of rails): "))
    encrypted_text = rail_fence_encrypt(plain_text, key)
    print("Encrypted text:", encrypted_text)
    decrypted_text = rail_fence_decrypt(encrypted_text, key)
    print("Decrypted text:", decrypted_text)


if __name__ == "__main__":
    main()
