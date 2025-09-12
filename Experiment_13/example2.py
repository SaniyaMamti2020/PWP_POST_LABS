file_path = "example.txt"

lines_list = []
with open(file_path, "r") as f:
    for line in f:
        lines_list.append(line.strip())

print("List of lines:", lines_list)

print("\n3EK3_16_Saniya_Mamti")