import sympy as sp

n, z, w = sp.symbols('n z w')
x_n = sp.cos(w*n) * sp.Heaviside(n)
X_z = sp.summation(x_n * z**(-n), (n, 0, sp.oo))

print("Z-transform of x[n] = cos(wn) u[n]:", X_z)
print("\n 3EK3_16_Saniya_Mamti")