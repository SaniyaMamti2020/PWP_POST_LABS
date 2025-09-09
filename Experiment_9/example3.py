import pandas as pd
import numpy as np

# From List
list_data = [1, 2, 3, 4, 5]
s_list = pd.Series(list_data)
print("Series from List:\n", s_list)

# From NumPy Array
array_data = np.array([10, 20, 30, 40, 50])
s_array = pd.Series(array_data)
print("\nSeries from NumPy Array:\n", s_array)

# From Dictionary
dict_data = {'x': 100, 'y': 200, 'z': 300}
s_dict = pd.Series(dict_data)
print("\nSeries from Dictionary:\n", s_dict)

print("\n", "Ek_3_Saniya_Mamti_16")