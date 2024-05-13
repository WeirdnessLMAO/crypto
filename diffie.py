def mod_exp(base, exponent, modulus):
    result = 1
    base = base % modulus
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent = exponent // 2
        base = (base * base) % modulus
    return result

def generate_key(prime, primitive_root):
    private_key = int(input("Enter your private key: "))
    public_key = mod_exp(primitive_root, private_key, prime)
    return private_key, public_key

def compute_shared_secret(private_key, other_public_key, prime):
    shared_secret = mod_exp(other_public_key, private_key, prime)
    return shared_secret

def main():
    prime = int(input("Enter the prime number (p): "))
    primitive_root = int(input("Enter the primitive root (g): "))

    print("\nAlice's side:")
    alice_private_key, alice_public_key = generate_key(prime, primitive_root)
    print("Alice's private key:", alice_private_key)
    print("Alice's public key:", alice_public_key)

    print("\nBob's side:")
    bob_private_key, bob_public_key = generate_key(prime, primitive_root)
    print("Bob's private key:", bob_private_key)
    print("Bob's public key:", bob_public_key)

    print("\nComputing shared secret...")
    alice_shared_secret = compute_shared_secret(alice_private_key, bob_public_key, prime)
    bob_shared_secret = compute_shared_secret(bob_private_key, alice_public_key, prime)

    print("\nShared secret computed by Alice:", alice_shared_secret)
    print("Shared secret computed by Bob:", bob_shared_secret)

    if alice_shared_secret == bob_shared_secret:
        print("\nShared secret matched! Secure communication established.")
    else:
        print("\nShared secret mismatch! Failed to establish secure communication.")

if __name__ == "__main__":
    main()
