with open("source.txt", "r") as src, open("destination.txt", "w") as dest:
    for line in src:
        dest.write(line)
print("File copied successfully!")
