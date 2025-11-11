# Beginner-friendly RSA example

# Step 1: Key generation
p = 3
q = 11
n = p * q                  # Modulus
phi = (p - 1) * (q - 1)    # Euler's totient

e = 7                       # Public exponent (coprime with phi)

# Step 1a: Find d (modular inverse of e modulo phi) using simple loop
d = 1
while (d * e) % phi != 1:
    d += 1

# Display keys
print(f"Public key (e, n): ({e}, {n})")
print(f"Private key (d, n): ({d}, {n})")
print(f"Value of d: {d}")

# Step 2: Encryption
M = 31                      # Message
C = pow(M, e, n)            # Modular exponentiation
print(f"Encrypted message: {C}")

# Step 3: Decryption
decrypted = pow(C, d, n)    # Modular exponentiation
print(f"Decrypted message: {decrypted}")
