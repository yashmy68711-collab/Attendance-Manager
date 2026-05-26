import tkinter as tk
from tkinter import messagebox

# Save Attendance
def save_attendance():
    name = name_entry.get().strip()
    status = attendance_var.get()

    # Validation
    if name == "":
        messagebox.showerror(
            "Error",
            "Enter student name"
        )
        return

    # Save to file
    with open("attendance.txt", "a") as file:
        file.write(f"{name} - {status}\n")

    messagebox.showinfo(
        "Saved",
        "Attendance saved successfully!"
    )

    # Clear input
    name_entry.delete(0, tk.END)

    # Status update
    status_label.config(
        text="Attendance saved successfully!"
    )

# Clear Function
def clear_name():
    name_entry.delete(0, tk.END)

# Window
window = tk.Tk()
window.title("Attendance Manager")
window.geometry("400x350")

# Title
title = tk.Label(
    window,
    text="Attendance Manager",
    font=("Arial", 16, "bold")
)

title.pack(pady=15)

# Name Entry
tk.Label(window, text="Student Name").pack()

name_entry = tk.Entry(window, width=30)
name_entry.pack(pady=5)

# Attendance Option
attendance_var = tk.StringVar()
attendance_var.set("Present")

tk.Radiobutton(
    window,
    text="Present",
    variable=attendance_var,
    value="Present"
).pack()

tk.Radiobutton(
    window,
    text="Absent",
    variable=attendance_var,
    value="Absent"
).pack()

# Save Button
save_btn = tk.Button(
    window,
    text="Save Attendance",
    command=save_attendance,
    width=20
)

save_btn.pack(pady=10)

# Clear Button
clear_btn = tk.Button(
    window,
    text="Clear",
    command=clear_name,
    width=20
)

clear_btn.pack(pady=5)

# Status Label
status_label = tk.Label(
    window,
    text="Attendance Manager Ready",
    font=("Arial", 10)
)

status_label.pack(pady=10)

# Run
window.mainloop()
