import pandas as pd

# Two Series
s1 = pd.Series([1, 2, 3, 4])
s2 = pd.Series([5, 6, 7, 8])

# Stack Vertically
vertical_stack = pd.concat([s1, s2], axis=0)
print("Vertical Stack:\n", vertical_stack)

# Stack Horizontally
horizontal_stack = pd.concat([s1, s2], axis=1)
print("\nHorizontal Stack:\n", horizontal_stack)
print("\n", "Ek_3_Saniya_Mamti_16")