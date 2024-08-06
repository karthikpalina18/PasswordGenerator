import tkinter as tk
import random
import string
import pyperclip  # To copy password to clipboard

def generate_password():
    length = int(length_entry.get())
    include_upper = upper_var.get()
    include_lower = lower_var.get()
    include_digits = digits_var.get()
    include_special = special_var.get()

    characters = ''
    if include_upper:
        characters += string.ascii_uppercase
    if include_lower:
        characters += string.ascii_lowercase
    if include_digits:
        characters += string.digits
    if include_special:
        characters += string.punctuation

    if not characters:
        password_label.config(text="Select at least one character type!")
        return

    password = ''.join(random.choice(characters) for _ in range(length))
    password_label.config(text=password)

def copy_to_clipboard():
    password = password_label.cget("text")
    if password:
        pyperclip.copy(password)

# Create GUI
window = tk.Tk()
window.title("Advanced Password Generator")

tk.Label(window, text="Password Length:").grid(row=0, column=0)
length_entry = tk.Entry(window)
length_entry.grid(row=0, column=1)

upper_var = tk.BooleanVar()
tk.Checkbutton(window, text="Include Uppercase", variable=upper_var).grid(row=1, column=0, columnspan=2)

lower_var = tk.BooleanVar()
tk.Checkbutton(window, text="Include Lowercase", variable=lower_var).grid(row=2, column=0, columnspan=2)

digits_var = tk.BooleanVar()
tk.Checkbutton(window, text="Include Digits", variable=digits_var).grid(row=3, column=0, columnspan=2)

special_var = tk.BooleanVar()
tk.Checkbutton(window, text="Include Special Characters", variable=special_var).grid(row=4, column=0, columnspan=2)

generate_button = tk.Button(window, text="Generate Password", command=generate_password)
generate_button.grid(row=5, column=0, columnspan=2)

password_label = tk.Label(window, text="", wraplength=300)
password_label.grid(row=6, column=0, columnspan=2)

copy_button = tk.Button(window, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.grid(row=7, column=0, columnspan=2)

window.mainloop()
