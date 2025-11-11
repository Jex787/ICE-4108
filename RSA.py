# Simple RSA Encryption/Decryption
p, q = 17, 19
n = p * q
phi = (p - 1) * (q - 1)
e = 5
d = pow(e, -1, phi)

msg = int(input("Enter a number message: "))

# Encryption
cipher = pow(msg, e, n)

# Decryption
decrypted = pow(cipher, d, n)

print("Public key (e, n):", (e, n))
print("Private key (d, n):", (d, n))
print("Encrypted message:", cipher)
print("Decrypted message:", decrypted)
