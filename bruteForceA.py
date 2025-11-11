# Brute-force Caesar attack with simple automatic detection
ct = input("Cipher Text: ").lower()

# Words to look for in candidate plaintexts (expand as needed)
W = {'the', 'and', 'is', 'you', 'meet', 'attack', 'secret', 'hello', 'password', 'flag'}

for s in range(26):
    pt = ''.join(
        chr((ord(c) - 97 - s) % 26 + 97) if 'a' <= c <= 'z' else c
        for c in ct
    )
    # If any dictionary word appears as a whole word, underline the candidate
    mark = any(w in pt.split() for w in W)
    print(f"{s:2}: " + (f"\x1b[4m{pt}\x1b[0m" if mark else pt))
