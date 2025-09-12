file1 = "file1.txt"
file2 = "file2.txt"
merged = "merged.txt"

with open(file1, "r") as f1, open(file2, "r") as f2, open(merged, "w") as f3:
    f3.write(f1.read())
    f3.write("\n")
    f3.write(f2.read())

print("Files merged into merged.txt")
print("\n3EK3_16_Saniya_Mamti")