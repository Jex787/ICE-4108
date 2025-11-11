# Diffie–Hellman Key Exchange Algorithm

q = int(input("Enter a prime number (q): "))
alpha = int(input("Enter a primitive root of q (α): "))
XA = int(input("Enter private key for User A (XA): "))
XB = int(input("Enter private key for User B (XB): "))

# put q=7,alpha=5,XA=3 and XA=4)

# Public keys

YA = pow(alpha, XA, q)    # User A's public key
YB = pow(alpha, XB, q)    # User B's public key

# Shared secret keys
KA = pow(YB, XA, q)       # Secret key computed by User A
KB = pow(YA, XB, q)       # Secret key computed by User B

print("---- Diffie–Hellman Key Exchange algo ----")
print("-------------------------------------------")
print(f"Secret Key by User A(KA) : {KA}")
print(f"Secret Key by User B (KB): {KB}")


# Verify keys
if KA == KB:
    print(f"✅ Shared Secret Key Established Successfully: K = {KA}")
else:
    print("❌ Error: Secret keys do not match!")












