# Simple modular arithmetic using primitive roots

# Choose a prime number
p = 10

# Choose a candidate primitive root
g = 3

# List to store powers modulo p
mod_results = []

# Compute g^1, g^2, ..., g^(p-1) modulo p
for i in range(1, p):
    mod_val = (g ** i) % p
    mod_results.append(mod_val)
    print(f"{g}^{i} mod {p} = {mod_val}")

# Check if all numbers from 1 to p-1 appear
is_primitive = sorted(mod_results) == list(range(1, p))
if is_primitive:
    print(f"\n{g} is a primitive root modulo {p}.")
else:
    print(f"\n{g} is NOT a primitive root modulo {p}.")
