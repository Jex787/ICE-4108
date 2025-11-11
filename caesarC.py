# Caesar Cipher Encryption and Decryption
t = input("Enter text: ")
s = int(input("Enter shift value: "))

# Encryption and Decryption using lambda function
c = lambda x, y: ''.join(
    chr((ord(i.upper()) - 65 + y) % 26 + 65) if i.isalpha() else i 
    for i in x
)

# Display results
print("Encrypted:", c(t, s))
print("Decrypted:", c(c(t, s), -s))
