def count_digits(number):
    # Handle negative numbers by converting to positive
    number = abs(number)
    
    # Special case for 0
    if number == 0:
        return 1
    
    count = 0
    while number > 0:
        number //= 10  # Remove the last digit
        count += 1
    return count

# Take input from the user
num = int(input("Enter a number: "))
print("Number of digits:", count_digits(num))
print("\n", "Ek_3_Saniya_Mamti_16")