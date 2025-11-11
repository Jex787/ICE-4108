# Monoalphabetic Substitution Cipher (Encryption & Decryption)
a = "abcdefghijklmnopqrstuvwxyz"
b = "qwertyuiopasdfghjklzxcvbnm"

m = input("Enter message: ").lower()

# Encryption
e = "".join([b[a.index(c)] if c in a else c for c in m])

# Decryption
d = "".join([a[b.index(c)] if c in b else c for c in e])

# Display results
print("Encrypted:", e)
print("Decrypted:", d)
