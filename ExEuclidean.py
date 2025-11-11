# Extended Euclidean ALgorithm
def egcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x, y = egcd(b, a % b)
    return g, y, x - (a // b) * y

# Input from user
a, b = map(int, input("Enter a b: ").split())

# Compute gcd and coefficients
g, x, y = egcd(a, b)
print(f"gcd = {g}, x = {x}, y = {y}")
