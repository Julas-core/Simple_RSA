from RSA_Improved import encrypt, decrypt, is_prime, generate_e_suggestions
import math

# Test Primes
assert is_prime(17) == True
assert is_prime(4) == False

# Test RSA Math from README
p = 17
q = 11
n = p * q
phi = (p-1) * (q-1)
e = 7

# Key generation logic check
assert math.gcd(e, phi) == 1
d = pow(e, -1, phi)

pub_key = (e, n)
priv_key = (d, n)

msg = "HI"
# Encrypt
cipher = encrypt(pub_key, msg)
print(f"Encrypted 'HI': {cipher}")

# Decrypt
decrypted = decrypt(priv_key, cipher)
print(f"Decrypted: {decrypted}")

assert decrypted == "HI"
print("Test Passed!")
