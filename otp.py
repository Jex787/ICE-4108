# One-Time Pad Encryption and Decryption
t = input("Enter text: ").upper()
k = input("Enter key (same length as text): ").upper()

# Function for encryption (+1) and decryption (-1)
f = lambda s, key, m: ''.join(
    chr((ord(a) - 65 + m * (ord(b) - 65)) % 26 + 65) if a.isalpha() else a
    for a, b in zip(s, key)
)

# Encryption
c = f(t, k, 1)
print("Encrypted:", c)

# Decryption
print("Decrypted:", f(c, input("Enter key again: ").upper(), -1))
