import tkinter as tk
from tkinter import messagebox


def calculate_age():
    name = name_entry.get().strip()
    if not name:
        messagebox.showerror("Missing name", "Please enter your name.")
        return

    try:
        birth_year = int(year_entry.get())
    except ValueError:
        messagebox.showerror("Invalid year", "Please enter a valid birth year.")
        return

 
    # Use the real current year dynamically
    current_year = __import__('datetime').datetime.now().year
    age = current_year - birth_year
    age_in_months = age * 12

    if age < 0:
        status = "time traveler"
    elif age < 18:
        status = "minor"
    else:
        status = "adult"

    result_var.set(
        f"Hello, {name}!\n"
        f"You are approximately {age} years old ({status}), or "
        f"about {age_in_months} months old."
    )


window = tk.Tk()
window.title("Age Calculator")
window.geometry("400x250")
window.resizable(False, False)

frame = tk.Frame(window, padx=20, pady=20)
frame.pack(fill="both", expand=True)

name_label = tk.Label(frame, text="Name:", font=("Arial", 11))
name_label.grid(row=0, column=0, sticky="w", pady=(0, 10))

name_entry = tk.Entry(frame, width=30, font=("Arial", 11))
name_entry.grid(row=0, column=1, pady=(0, 10))

year_label = tk.Label(frame, text="Birth year:", font=("Arial", 11))
year_label.grid(row=1, column=0, sticky="w", pady=(0, 10))

year_entry = tk.Entry(frame, width=30, font=("Arial", 11))
year_entry.grid(row=1, column=1, pady=(0, 10))

calculate_button = tk.Button(frame, text="Calculate", command=calculate_age, font=("Arial", 11))
calculate_button.grid(row=2, column=0, columnspan=2, pady=(10, 15), sticky="ew")

result_var = tk.StringVar(value="Your result will appear here.")
result_label = tk.Label(frame, textvariable=result_var, justify="left", font=("Arial", 10), fg="darkgreen")
result_label.grid(row=3, column=0, columnspan=2, sticky="w")

window.mainloop() 