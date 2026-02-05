import math

print("MY RSA ENCRYPTON\n")

p = int(input("Enter first prime number: "))
q = int(input("Enter second prime number: "))
print(" ")

n = p * q
phi = (p - 1) * (q - 1)

print("n =", n)
print("phi =", phi)

print("possible values of e : ")

print(" ")
print("[")

for i in range(2,phi):
    if math.gcd(i,phi)==1:
            print(i, end=",")
print("]")
print(" ")
e = int(input("Enter public key e: "))

### it checks if e (the public key) is valid  ###
if math.gcd(e, phi) != 1:
    print("e is not coprime with phi. Try again.")
    quit()

### find d (the private key) ###
d = 0
for i in range(1, phi):
    if (e * i) % phi == 1:
        d = i
        break

print("Public Key:", e)
print("Your Private Key:", d)

print(" ")

choice = input("Encrypt or Decrypt (e/d): ")

############# ENCRYPT #############
print(" ")
if choice == "e" or choice == "E":
    text = input("Enter message: ")
    cipher = ""

    for ch in text:
        c = pow(ord(ch), e, n)
        cipher = cipher + str(c) + " "
    print(" ")
    print("Encrypted:")
    print(cipher)

############## DECRYPT ##############
elif choice == "d" or choice == "D":
    cipher_text = input("Enter encrypted numbers separated by space: ")
    numbers = cipher_text.split()
    message = ""

    for num in numbers:
        m = pow(int(num), d, n)
        message = message + chr(m)

    print("Decrypted:")
    print(message)

else:
    print("Wrong choice")