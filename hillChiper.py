# Hill Chiper
import numpy as np
 
# Key matrix (must be invertible mod 26)
k = np.array([[3, 3], [2, 5]])

def hi(m, enc=True):
    # Prepare message: uppercase, remove spaces, and pad if odd length
    m = m.upper().replace(" ", "") + ("X" * (len(m) % 2))

    # Compute encryption or decryption matrix
    K = k if enc else (pow(int(round(np.linalg.det(k))), -1, 26) * 
                      np.array([[k[1,1], -k[0,1]], [-k[1,0], k[0,0]]])) % 26

    # Encrypt or decrypt pairs of letters
    r = ""
    for i in range(0, len(m), 2):
        r += "".join(chr(int(x) + 65) for x in np.dot(K, [ord(m[i]) - 65, ord(m[i+1]) - 65]) % 26)
    return r

# Main program
x = input("Message: ")
e = hi(x)
print("Encode:", e)
print("Decode:", hi(e, False))
