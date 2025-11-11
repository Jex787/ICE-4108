# ElGamal Cryptographic Algorithm 

# User Inputs (example: p=23, g=5, x=6, M=10, k=7)
p = int(input("Enter prime number p: "))
g = int(input("Enter primitive root g: "))
x = int(input("Enter private key x: "))
M = int(input("Enter message M: "))
k = int(input("Enter random key k: "))

# Compute public key
y = pow(g, x, p)

# Encryption
C1 = pow(g, k, p)
C2 = (M * pow(y, k, p)) % p

# Decryption
M_decrypted = (C2 * pow(C1, p - 1 - x, p)) % p

# Output
print("\n--- Results ---")
print(f"Public Key (y): {y}")
print(f"Ciphertext (C1, C2): ({C1}, {C2})")
print(f"Decrypted Message: {M_decrypted}")
