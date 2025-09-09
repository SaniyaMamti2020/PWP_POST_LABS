# Take input from the user
num = int(input("Enter a number: "))

# Get the last digit using modulo
last_digit = abs(num) % 10

# Get the first digit by repeatedly dividing by 10
first_digit = abs(num)
while first_digit >= 10:
    first_digit //= 10

# Display the results
print("First digit:", first_digit)
print("Last digit:", last_digit)
print("\n", "Ek_3_Saniya_Mamti_16")