def read_large_file(filename):
    with open(filename, 'r') as file:
        for line in file:
            yield line.strip()

for line in read_large_file('data.txt'):
    print(line)
