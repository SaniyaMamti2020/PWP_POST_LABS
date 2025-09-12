import csv

file_path = "data-1.csv"

with open(file_path) as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)

print("\n3EK3_16_Saniya_Mamti")