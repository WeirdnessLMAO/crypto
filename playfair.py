def generate_playfair_matrix(key):
    # Create a 5x5 matrix initialized with zeros
    matrix = [['' for _ in range(5)] for _ in range(5)]
    
    # Remove duplicates from the key and combine with the alphabet
    key = ''.join(dict.fromkeys(key + 'abcdefghiklmnopqrstuvwxyz').keys())
    
    # Fill the matrix with the key and remaining alphabets
    i, j = 0, 0
    for char in key:
        if char == 'j':
            char = 'i'  # In Playfair, 'i' and 'j' are usually treated as the same
        matrix[i][j] = char
        j += 1
        if j == 5:
            i += 1
            j = 0
            
    alphabet = 'abcdefghiklmnopqrstuvwxyz'
    for char in alphabet:
        if char == 'j':
            continue
        matrix[i][j] = char
        j += 1
        if j == 5:
            i += 1
            j = 0
            
    return matrix

def get_char_position(matrix, char):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                return i, j
def playfair_encrypt(plain_text, key):
    plain_text = plain_text.replace(' ', '').lower()
    plain_text = plain_text.replace('j', 'i')  
    matrix = generate_playfair_matrix(key)
    encrypted_text = ""
    for i in range(0, len(plain_text), 2):
        pair1 = plain_text[i]
        pair2 = plain_text[i + 1] if i + 1 < len(plain_text) else 'x'
        if pair2 == pair1:
            pair2 = 'x'
        row1, col1 = get_char_position(matrix, pair1)
        row2, col2 = get_char_position(matrix, pair2)
        if row1 == row2:  
            encrypted_text += matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:
            encrypted_text += matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
        else:  
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
        if row1 == row2:  
            decrypted_text += matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
        elif col1 == col2: 
            decrypted_text += matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
        else: 
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



*WORK AGALANA USE THIS*

def prepare_text(text):
    text = text.replace(" ", "").upper()
    text = text.replace("J", "I")
    pairs = []
    i = 0
    while i < len(text):
        if i == len(text) - 1 or text[i] == text[i + 1]:
            pairs.append(text[i] + 'X')
            i += 1
        else:
            pairs.append(text[i] + text[i + 1])
            i += 2
    return pairs

def generate_key_square(key):
    key = key.upper().replace(" ", "")
    key = key.replace("J", "I")
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    key_square = ""
    for char in key:
        if char not in key_square:
            key_square += char
    for char in alphabet:
        if char not in key_square:
            key_square += char
    return key_square

def get_coordinates(key_square, letter):
    index = key_square.index(letter)
    row = index // 5
    col = index % 5
    return row, col

def encrypt(plaintext, key):
    key_square = generate_key_square(key)
    plaintext_pairs = prepare_text(plaintext)
    ciphertext = ""
    for pair in plaintext_pairs:
        row1, col1 = get_coordinates(key_square, pair[0])
        row2, col2 = get_coordinates(key_square, pair[1])
        if row1 == row2:
            ciphertext += key_square[row1 * 5 + (col1 + 1) % 5]
            ciphertext += key_square[row2 * 5 + (col2 + 1) % 5]
        elif col1 == col2:
            ciphertext += key_square[((row1 + 1) % 5) * 5 + col1]
            ciphertext += key_square[((row2 + 1) % 5) * 5 + col2]
        else:
            ciphertext += key_square[row1 * 5 + col2]
            ciphertext += key_square[row2 * 5 + col1]
    return ciphertext

def decrypt(ciphertext, key):
    key_square = generate_key_square(key)
    plaintext_pairs = prepare_text(ciphertext)
    plaintext = ""
    for pair in plaintext_pairs:
        row1, col1 = get_coordinates(key_square, pair[0])
        row2, col2 = get_coordinates(key_square, pair[1])
        if row1 == row2:
            plaintext += key_square[row1 * 5 + (col1 - 1) % 5]
            plaintext += key_square[row2 * 5 + (col2 - 1) % 5]
        elif col1 == col2:
            plaintext += key_square[((row1 - 1) % 5) * 5 + col1]
            plaintext += key_square[((row2 - 1) % 5) * 5 + col2]
        else:
            plaintext += key_square[row1 * 5 + col2]
            plaintext += key_square[row2 * 5 + col1]
    return plaintext

def main():
    plaintext = input("Enter the plaintext: ")
    key = input("Enter the key: ")
    encrypted_text = encrypt(plaintext, key)
    print("Encrypted:", encrypted_text)
    
    key_decrypt = input("Enter the key: ")
    encrypted_text_decrypt = input("Enter the encrypted text: ")
    decrypted_text = decrypt(encrypted_text_decrypt, key_decrypt)
    print("Decrypted:", decrypted_text)

if _name_ == "_main_":
    main()
