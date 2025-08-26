import math as m

def evaluate_functions(x):
    f = m.cos(2 * x)
    f_prime = -2 * m.sin(2 * x)
    f_double_prime = -4 * m.cos(2 * x)
    return f, f_prime, f_double_prime

# Evaluate for x = π
x = m.pi
f, f_prime, f_double_prime = evaluate_functions(x)
print(f"f(x) = {f}")
print(f"f'(x) = {f_prime}")
print(f"f''(x) = {f_double_prime}")

print("\nEk_3_Saniya_Mamti_16")