file_path = "example.txt"

with open(file_path, "r") as f:
    text = f.read()

line_count = text.count("\n") + 1 if text else 0
word_count = len(text.split())
char_count = len(text)

print(f"Lines: {line_count}")
print(f"Words: {word_count}")
print(f"Characters: {char_count}")

print("\n3EK3_16_Saniya_Mamti")