# def extended_gcd(a, b):
#     if a == 0:
#         return b, 0, 1
#     else:
#         gcd, x1, y1 = extended_gcd(b % a, a)
#         x = y1 - (b // a) * x1
#         y = x1
#         return gcd, x, y


# # Example values
# a = 35
# b = 21

# gcd, x, y = extended_gcd(a, b)
# print(f"GCD({a}, {b}) = {gcd}\nBézout coefficients: x = {x}, y = {y}")



#Extended Euclidean Algorithm (with user input)

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x1, y1 = extended_gcd(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return gcd, x, y


# --- User Input ---
a = int(input("Enter the first number (a): "))
b = int(input("Enter the second number (b): "))

# --- Function Call ---
gcd, x, y = extended_gcd(a, b)

# --- Output ---
print(f"\nGCD({a}, {b}) = {gcd}")
print(f"Bézout coefficients: x = {x}, y = {y}")
print(f"Verification: {a}({x}) + {b}({y}) = {a*x + b*y}")
