# Input from user
sentence = input("Enter a sentence: ")

# Remove leading/trailing spaces and split the sentence into words
words = sentence.strip().split()

# Check if there are any words
if words:
    last_word = words[-1]
    print("The last word is:", last_word)
    print("Length of the last word:", len(last_word), "\n")
else:
    print("The sentence is empty or has no words.", "\n")

print("Ek_3_Saniya_Mamti")