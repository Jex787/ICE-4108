# XOR Encryption/Decryption (simple DES-like)
k = input("Key: ")
t = input("Text: ")

# Encryption
e = bytes([ord(t[i]) ^ ord(k[i % len(k)]) for i in range(len(t))])
print("Encrypted (hex):", e.hex())

# Decryption
d = bytes([e[i] ^ ord(k[i % len(k)]) for i in range(len(e))])
print("Decrypted:", d.decode())
