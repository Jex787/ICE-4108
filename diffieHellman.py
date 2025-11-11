# Diffie-Hellman Key Exchange + XOR Encryption
p, g = 23, 5  # Public parameters
a = int(input("Alice's private key: "))
b = int(input("Bob's private key: "))

A = pow(g, a, p)  # Alice's public key
B = pow(g, b, p)  # Bob's public key

# Shared secret
s = pow(B, a, p)  # same as pow(A, b, p)
print("Shared secret:", s)

# Simple XOR encryption/decryption
msg = input("Message: ")
enc = ''.join(chr(ord(c) ^ s) for c in msg)
dec = ''.join(chr(ord(c) ^ s) for c in enc)

print("Encrypted:", enc)
print("Decrypted:", dec)
