# Define a list
elements = [1, 2, 2, 3, 1, 4, 2, 3, 4, 4]

# Create an empty dictionary to store frequency
frequency = {}

# Loop through the list and count frequency
for item in elements:
    if item in frequency:
        frequency[item] += 1
    else:
        frequency[item] = 1

# Print the result
print("Frequency of elements:", frequency)
print("\n", "Ek_3_Saniya_Mamti")