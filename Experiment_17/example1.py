import sympy as sp

n, z = sp.symbols('n z')
a = 3
x_n = a**n * sp.Heaviside(n)
X_z = sp.summation(x_n * z**(-n), (n, 0, sp.oo))

print("Z-transform of x[n] = 3^n u[n]:", X_z)
print("\n 3EK3_16_Saniya_Mamti")