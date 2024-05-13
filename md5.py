import hashlib
def calculate_sha1(text):
    md5_hash = hashlib.md5(text.encode()).hexdigest()
    return md5_hash
def main():
    text = input("Enter the text to calculate MD-5 hash: ")
    sha1_hash = calculate_sha1(text)
    print("MD-5 hash of the text:", sha1_hash)
if __name__ == "__main__":
    main() 
