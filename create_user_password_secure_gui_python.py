import random
import string
import tkinter as tk


def generate_random_username(num_chars):
    username = ''.join(random.choices(string.ascii_letters + string.digits, k=num_chars))
    # Check if there are any spaces in the generated username
    if ' ' in username:
        return generate_random_username(num_chars)
    return username


def generate_strong_password(num_chars):
    password_chars = string.ascii_letters + string.digits + "!@#$%^&*()_-+=[]{}|;:,.<>?/"
    password = ''.join(random.choices(password_chars, k=num_chars))
    # Check if there are any spaces in the generated password
    if ' ' in password:
        return generate_strong_password(num_chars)
    return password


def generate_credentials():
    username = generate_random_username(username_chars.get())
    password = generate_strong_password(password_chars.get())
    username_display.delete("1.0", tk.END)
    username_display.insert(tk.END, username)
    password_display.delete("1.0", tk.END)
    password_display.insert(tk.END, password)


# Main window configuration
root = tk.Tk()
root.title("Credentials Generator")
root.geometry("400x250")

# Variables to store the number of characters for username and password
username_chars = tk.IntVar()
password_chars = tk.IntVar()

# Widgets
username_label = tk.Label(root, text="Number of Characters for Username:", font=("Helvetica", 12))
password_label = tk.Label(root, text="Number of Characters for Password:", font=("Helvetica", 12))

username_entry = tk.Entry(root, textvariable=username_chars)
password_entry = tk.Entry(root, textvariable=password_chars)

generate_button = tk.Button(root, text="Generate Credentials", command=generate_credentials)

# Display text boxes for the generated username and password
username_display = tk.Text(root, height=1, width=30)
password_display = tk.Text(root, height=1, width=30)

# Widget positioning
username_label.pack(pady=10)
username_entry.pack(pady=5)
password_label.pack(pady=10)
password_entry.pack(pady=5)
generate_button.pack(pady=10)
username_display.pack(pady=5)
password_display.pack(pady=5)

# Main graphical interface loop
root.mainloop()
