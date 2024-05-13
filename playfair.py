def generate_playfair_matrix(key):
    # Create a 5x5 matrix initialized with zeros
    matrix = [['' for _ in range(5)] for _ in range(5)]
    # Remove duplicates from the key and combine with the alphabet
    key = ''.join(dict.fromkeys(key + 'abcdefghijklmnopqrstuvwxyz').keys())
    # Fill the matrix with the key and remaining alphabets
    alphabet = 'abcdefghiklmnopqrstuvwxyz'
    i, j = 0, 0
    for char in key:
        if char == 'j':
            char = 'i'  # In Playfair, 'i' and 'j' are usually treated as the same
        matrix[i][j] = char
        j += 1
        if j == 5:
            i += 1
            j = 0
            if i == 5:  # Ensure i does not exceed 4
                break
    for char in alphabet:
        if char == 'j':
            continue
        matrix[i][j] = char
        j += 1
        if j == 5:
            i += 1
            j = 0
            if i == 5:  # Ensure i does not exceed 4
                break
    return matrix


def get_char_position(matrix, char):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                return i, j


def playfair_encrypt(plain_text, key):
    plain_text = plain_text.replace(' ', '').lower()
    plain_text = plain_text.replace('j', 'i')  # Replace 'j' with 'i'
    matrix = generate_playfair_matrix(key)
    encrypted_text = ""
    for i in range(0, len(plain_text), 2):
        pair1 = plain_text[i]
        pair2 = plain_text[i + 1] if i + 1 < len(plain_text) else 'x'
        if pair2 == pair1:
            pair2 = 'x'
        row1, col1 = get_char_position(matrix, pair1)
        row2, col2 = get_char_position(matrix, pair2)
        if row1 == row2:  # Same row
            encrypted_text += matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:  # Same column
            encrypted_text += matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
        else:  # Forming a rectangle
            encrypted_text += matrix[row1][col2] + matrix[row2][col1]
    return encrypted_text.upper()


def playfair_decrypt(cipher_text, key):
    matrix = generate_playfair_matrix(key)
    decrypted_text = ""
    for i in range(0, len(cipher_text), 2):
        pair1 = cipher_text[i]
        pair2 = cipher_text[i + 1]
        row1, col1 = get_char_position(matrix, pair1)
        row2, col2 = get_char_position(matrix, pair2)
        if row1 == row2:  # Same row
            decrypted_text += matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:  # Same column
            decrypted_text += matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
        else:  # Forming a rectangle
            decrypted_text += matrix[row1][col2] + matrix[row2][col1]
    return decrypted_text.replace('x', '')


def main():
    key = input("Enter the key for Playfair cipher: ").lower()
    plain_text = input("Enter the plain text: ").lower()
    encrypted_text = playfair_encrypt(plain_text, key)
    print("Encrypted text:", encrypted_text)
    decrypted_text = playfair_decrypt(encrypted_text, key)
    print("Decrypted text:", decrypted_text)


if __name__ == "__main__":
    main()
5
