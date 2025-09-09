# Take input from the user
num = int(input("Enter a number: "))

# Convert number to string for easy swapping
num_str = str(num)

# If number has only one digit, swapping doesn't change it
if len(num_str) == 1:
    swapped_num = num_str
else:
    # Swap first and last digits
    swapped_num = num_str[-1] + num_str[1:-1] + num_str[0]

# Convert back to integer
swapped_num = int(swapped_num)

# Display result
print("Number after swapping first and last digits:", swapped_num)
print("\n", "Ek_3_Saniya_Mamti_16")