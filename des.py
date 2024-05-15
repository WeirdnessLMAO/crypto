from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from base64 import b64encode, b64decode
def des_encrypt(key, plain_text):
    cipher = DES.new(key, DES.MODE_ECB)
    padded_plain_text = pad(plain_text, DES.block_size)
    cipher_text = cipher.encrypt(padded_plain_text)
    return b64encode(cipher_text)
def des_decrypt(key, cipher_text):
    cipher = DES.new(key, DES.MODE_ECB)
    decrypted_text = cipher.decrypt(b64decode(cipher_text))
    return unpad(decrypted_text, DES.block_size)
def main():
    key = get_random_bytes(8) # Generate a random 8-byte key
    plain_text = b"Hello, DES!"
    cipher_text = des_encrypt(key, plain_text)
    print("Encrypted text:", cipher_text)
    decrypted_text = des_decrypt(key, cipher_text)
    print("Decrypted text:", decrypted_text.decode())
if __name__ == "__main__":
    main()
