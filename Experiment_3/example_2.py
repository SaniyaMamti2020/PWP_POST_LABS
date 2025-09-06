string = input("Enter a string: ")

# Remove spaces and convert to lowercase for accurate comparison
processed_string = string.replace(" ", "").lower()

# Check if the string is equal to its reverse
if processed_string == processed_string[::-1]:
    print("The string is a palindrome.", "\n")
else:
    print("The string is not a palindrome.", "\n")
    
print("Ek_3_Saniya_Mamti")