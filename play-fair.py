# Playfair Cipher 
def mat(k):
    k = k.upper().replace("J", "I")
    a = "".join(dict.fromkeys(k + "ABCDEFGHIKLMNOPQRSTUVWXYZ"))
    return [a[i:i+5] for i in range(0, 25, 5)]

def pf(m, k, e=1):
    mt = mat(k)
    m = "".join(c for c in m.upper().replace("J", "I") if c.isalpha())
    r = ""
    i = 0
    while i < len(m):
        a, b = m[i], m[i+1] if i+1 < len(m) else "X"
        if a == b: b, i = "X", i+1
        else: i += 2
        x1, y1 = [(x, y) for x in range(5) for y in range(5) if mt[x][y]==a][0]
        x2, y2 = [(x, y) for x in range(5) for y in range(5) if mt[x][y]==b][0]
        if x1==x2: r += mt[x1][(y1+e)%5] + mt[x2][(y2+e)%5]
        elif y1==y2: r += mt[(x1+e)%5][y1] + mt[(x2+e)%5][y2]
        else: r += mt[x1][y2] + mt[x2][y1]
    return r

k = input("Key: ")
m = input("Message: ")
e = pf(m, k)
print("Encode:", e)
print("Decode:", pf(e, k, -1))
# print("Dec:", pf(e, k, -1).replace("X", ""))

