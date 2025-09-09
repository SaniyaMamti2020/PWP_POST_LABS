# Take input from the user
num = int(input("Enter a number: "))

# Work with absolute value for reversing, handle negative later
is_negative = num < 0
num = abs(num)

reverse_num = 0

# Reverse the digits
while num > 0:
    digit = num % 10
    reverse_num = reverse_num * 10 + digit
    num //= 10

# Add negative sign back if needed
if is_negative:
    reverse_num = -reverse_num

# Display the result
print("Reversed number:", reverse_num)
print("\n", "Ek_3_Saniya_Mamti_16")