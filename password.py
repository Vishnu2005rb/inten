import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password(length):
  
    characters = string.ascii_letters + string.digits + string.punctuation
    

    password = ''.join(random.choice(characters) for i in range(length))
    
    return password

def on_generate_button_click():
    try:
        length = int(entry_length.get())
        if length <= 0:
            raise ValueError("Length must be positive")
        password = generate_password(length)
        messagebox.showinfo("Generated Password", f"Your generated password is:\n{password}")
    except ValueError as e:
        messagebox.showerror("Invalid Input", f"Please enter a valid number for the length.\n{e}")


app = tk.Tk()
app.title("Password is Generator")


label_length = tk.Label(app, text="Enter the length of  password:")
label_length.pack(pady=5)

entry_length = tk.Entry(app)
entry_length.pack(pady=5)

generate_button = tk.Button(app, text="Generate the Password", command=on_generate_button_click)
generate_button.pack(pady=10)


app.mainloop()
