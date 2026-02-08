import math

def is_prime(n):
    """Checks if a number is prime."""
    if n <= 1: return False
    if n <= 3: return True
    if n % 2 == 0 or n % 3 == 0: return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def generate_e_suggestions(phi, limit=10):
    """Finds the first few valid values for e."""
    suggestions = []
    for i in range(2, phi):
        if math.gcd(i, phi) == 1:
            suggestions.append(i)
            if len(suggestions) >= limit:
                break
    return suggestions

def get_keys():
    """Interactively gets p, q, and e to generate keys."""
    try:
        print("--- Key Generation ---")
        p = int(input("Enter first prime number (p): "))
        if not is_prime(p):
            print(f"Error: {p} is not a prime number.")
            return None

        q = int(input("Enter second prime number (q): "))
        if not is_prime(q):
            print(f"Error: {q} is not a prime number.")
            return None

        if p == q:
            print("Error: p and q should be different.")
            return None

        n = p * q
        phi = (p - 1) * (q - 1)

        print(f"\nn = {n}")
        print(f"phi = {phi}")

        suggestions = generate_e_suggestions(phi)
        print(f"\nRecommended values for e: {suggestions} ...")
        
        e = int(input("Enter public key e: "))

        if math.gcd(e, phi) != 1:
            print("Error: e is not coprime with phi.")
            return None

        # Calculate private key d using modular inverse
        # d = e^-1 mod phi
        d = pow(e, -1, phi)

        return ((e, n), (d, n))
    except ValueError:
        print("Invalid input. Please enter numbers.")
        return None

def encrypt(public_key, plaintext):
    """Encrypts a string into a space-separated string of numbers."""
    e, n = public_key
    cipher_ints = [pow(ord(char), e, n) for char in plaintext]
    return ' '.join(map(str, cipher_ints))

def decrypt(private_key, ciphertext):
    """Decrypts a space-separated string of numbers back to a string."""
    d, n = private_key
    try:
        cipher_ints = map(int, ciphertext.split())
        plain_chars = [chr(pow(char, d, n)) for char in cipher_ints]
        return ''.join(plain_chars)
    except ValueError:
        return "Error: Invalid chipertext format."

def main():
    print("MY RSA ENCRYPTION (IMPROVED)\n")
    
    keys = get_keys()
    if not keys:
        return

    public_key, private_key = keys
    
    print(f"\nPublic Key (e, n): {public_key}")
    print(f"Private Key (d, n): {private_key}")

    while True:
        print("\n------------------------------")
        choice = input("Choose: [E]ncrypt, [D]ecrypt, [Q]uit: ").strip().upper()

        if choice == 'E':
            text = input("Enter message: ")
            encrypted_msg = encrypt(public_key, text)
            print(f"\nEncrypted: {encrypted_msg}")
        
        elif choice == 'D':
            cipher_text = input("Enter encrypted numbers (space separated): ")
            decrypted_msg = decrypt(private_key, cipher_text)
            print(f"\nDecrypted: {decrypted_msg}")
        
        elif choice == 'Q':
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
