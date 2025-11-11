# Transposition Cipher
def encrypt(msg, key):
    msg = msg.replace(" ", "").upper()
    cols = len(key)
    msg += "X" * ((cols - len(msg) % cols) % cols)
    matrix = [msg[i:i+cols] for i in range(0, len(msg), cols)]
    order = sorted(range(cols), key=lambda i: key[i])
    return ''.join(matrix[r][c] for c in order for r in range(len(matrix)))

m = input("Message: ")
k = input("Key: ")
print("Encrypted:", encrypt(m, k))
