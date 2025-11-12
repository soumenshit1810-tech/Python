import os

folder = "C:/Users/YourName/Desktop/test"
for count, filename in enumerate(os.listdir(folder)):
    src = os.path.join(folder, filename)
    dst = os.path.join(folder, f"file_{count}.txt")
    os.rename(src, dst)
print("Files renamed successfully!")
