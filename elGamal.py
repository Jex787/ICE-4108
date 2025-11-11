# ElGamal Encryption/Decryption
p, g, x, y = map(int, input("Enter p, g, x, y: ").split())  # x = private, y = public
m = int(input("Message: "))

# Encryption
k = 7  # session key (can also be random)
c1 = pow(g, k, p)
c2 = (m * pow(y, k, p)) % p
print(f"Encrypted: ({c1}, {c2})")

# Decryption
s = pow(c1, x, p)
m_dec = (c2 * pow(s, p - 2, p)) % p  # Modular inverse using Fermat's little theorem
print(f"Decrypted: {m_dec}")
