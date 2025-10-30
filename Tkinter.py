import tkinter as tk

root = tk.Tk()
root.title("Python GUI Example")

label = tk.Label(root, text="Hello, Python GUI!", font=("Arial", 16))
label.pack(pady=20)

button = tk.Button(root, text="Click Me", command=lambda: label.config(text="Button Clicked!"))
button.pack(pady=10)

root.mainloop()
