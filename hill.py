import numpy as np

# Function to convert text to numbers (A=0, B=1, ..., Z=25)
def text_to_numbers(text):
    return [ord(char.lower()) - ord('a') for char in text if char.isalpha()]

# Function to convert numbers to text
def numbers_to_text(numbers):
    return ''.join(chr(num + ord('a')) for num in numbers)

# Function to generate the key matrix from the key string
def generate_key_matrix(key):
    key = key.replace(' ', '').lower()
    key_len = len(key)
    matrix_dim = int(key_len ** 0.5)
    if matrix_dim ** 2 != key_len:
        raise ValueError("Key length must be a perfect square")
    key_matrix = np.array([ord(char) - ord('a') for char in key]).reshape((matrix_dim, matrix_dim))
    return key_matrix

# Function to encrypt plaintext using Hill Cipher
def hill_cipher_encrypt(plain_text, key_matrix):
    plain_text = plain_text.replace(' ', '').lower()
    plain_text = [ord(char) - ord('a') for char in plain_text if char.isalpha()]
    padding = len(plain_text) % key_matrix.shape[0]
    if padding > 0:
        plain_text += [0] * (key_matrix.shape[0] - padding)
    plain_text_matrix = np.array(plain_text).reshape((-1, key_matrix.shape[0]))
    encrypted_text_matrix = (plain_text_matrix @ key_matrix) % 26
    encrypted_text = numbers_to_text(encrypted_text_matrix.flatten())
    return encrypted_text.upper()

# Function to decrypt ciphertext using Hill Cipher
def hill_cipher_decrypt(cipher_text, key_matrix):
    cipher_text = cipher_text.replace(' ', '').lower()
    cipher_text = [ord(char) - ord('a') for char in cipher_text if char.isalpha()]
    cipher_text_matrix = np.array(cipher_text).reshape((-1, key_matrix.shape[0]))
    decrypted_text_matrix = np.dot(cipher_text_matrix, np.linalg.inv(key_matrix)).astype(int) % 26
    decrypted_text = numbers_to_text(decrypted_text_matrix.flatten())
    return decrypted_text.upper()


def main():
    key = input("Enter the key for Hill cipher (as a string of lowercase letters, no spaces): ")
    plain_text = input("Enter the plain text: ")
    try:
        key_matrix = generate_key_matrix(key)
    except ValueError as e:
        print(e)
        return
    encrypted_text = hill_cipher_encrypt(plain_text, key_matrix)
    print("Encrypted text:", encrypted_text)
    decrypted_text = hill_cipher_decrypt(encrypted_text, key_matrix)
    print("Decrypted text:", decrypted_text)

if __name__ == "__main__":
    main()
