import hashlib
def calculate_sha1(text):
    sha1_hash = hashlib.sha1(text.encode()).hexdigest()
    return sha1_hash
def main():
    text = input("Enter the text to calculate SHA-1 hash: ")
    sha1_hash = calculate_sha1(text)
    print("SHA-1 hash of the text:", sha1_hash)
if __name__ == "__main__":
    main() 
