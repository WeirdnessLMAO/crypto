from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from base64 import b64encode, b64decode
def aes_encrypt(key, plain_text):
    cipher = AES.new(key, AES.MODE_ECB)
    padded_plain_text = pad(plain_text, AES.block_size)
    cipher_text = cipher.encrypt(padded_plain_text)
    return b64encode(cipher_text)
def aes_decrypt(key, cipher_text):
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted_text = cipher.decrypt(b64decode(cipher_text))
    return unpad(decrypted_text, AES.block_size)
def main():
    key = get_random_bytes(16) # Generate a random 16-byte (128-bit) key for AES-128
    plain_text = b"Hello, AES!"
    cipher_text = aes_encrypt(key, plain_text)
    print("Encrypted text:", cipher_text)
    decrypted_text = aes_decrypt(key, cipher_text)
    print("Decrypted text:", decrypted_text.decode())
if __name__ == "__main__":
    main()
