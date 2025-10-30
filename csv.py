import csv

# Writing
with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Roll", "Marks"])
    writer.writerow(["Soumen", 1, 90])
    writer.writerow(["Ankit", 2, 85])

# Reading
with open("students.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
