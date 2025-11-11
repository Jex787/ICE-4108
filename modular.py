# Modular Arithmetic: Check primitive root
n, g = map(int, input("Enter n and g: ").split())
print(f"Checking if {g} is primitive root mod {n}:")
for i in range(1, n):
    r = pow(g, i, n)
    print(f"{g}^{i} mod {n} = {r}")
    if r == 1 and i != n-1:
        print(f"  Not a primitive root (repeats at {i})")
        break
else:
    print(f"  {g} is a primitive root of {n}")
