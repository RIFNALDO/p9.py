
"""
Length Converter App
Assignment: Where's the event? (Tkinter Library)
"""

import tkinter as tk
from tkinter import messagebox

# ── CONVERSION FUNCTION ──────────────────────────────────────
def convert_length():
    """Converts inches to centimeters and displays the result."""
    try:
        # Get value from entry field
        inches_text = entry_inches.get()
        
        # Check if input is empty
        if not inches_text.strip():
            messagebox.showerror("Error", "Please enter a value in inches!")
            return
        
        # Convert to float and calculate centimeters (1 inch = 2.54 cm)
        inches = float(inches_text)
        
        if inches < 0:
            messagebox.showerror("Error", "Length cannot be negative!")
            return
            
        cm = inches * 2.54
        
        # Display the result in the label
        result_label.config(text=f"{inches} inches = {cm:.2f} cm")
        
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid numeric value for inches.")

def clear_fields():
    """Clears the input entry and result label."""
    entry_inches.delete(0, tk.END)
    result_label.config(text="")

# ── MAIN WINDOW SETUP ────────────────────────────────────────
root = tk.Tk()
root.title("Length Converter App")
root.geometry("400x400")
root.config(bg="#f0f4f8")  # Soft background color

# Prevent window resizing for consistent layout
root.resizable(False, False)

# ── WIDGETS ──────────────────────────────────────────────────

# Title Header
title_label = tk.Label(
    root, 
    text="📏 Length Converter", 
    font=("Arial", 18, "bold"), 
    bg="#f0f4f8", 
    fg="#2c3e50"
)
title_label.pack(pady=30)

# Instruction Label
instructions = tk.Label(
    root, 
    text="Enter length in inches to convert to centimeters:", 
    font=("Arial", 10), 
    bg="#f0f4f8", 
    fg="#34495e"
)
instructions.pack(pady=5)

# Entry Field for Inches Input
entry_inches = tk.Entry(
    root, 
    font=("Arial", 14), 
    justify="center", 
    bd=2, 
    relief="solid"
)
entry_inches.pack(pady=10, ipady=4, ipadx=10)
entry_inches.focus()  # Focus cursor on entry field

# Convert Button
btn_convert = tk.Button(
    root, 
    text="Convert", 
    font=("Arial", 12, "bold"), 
    bg="#3498db", 
    fg="white", 
    activebackground="#2980b9",
    activeforeground="white",
    bd=0,
    padx=20,
    pady=8,
    command=convert_length
)
btn_convert.pack(pady=10)

# Clear Button
btn_clear = tk.Button(
    root, 
    text="Clear", 
    font=("Arial", 10), 
    bg="#95a5a6", 
    fg="white", 
    activebackground="#7f8c8d",
    activeforeground="white",
    bd=0,
    padx=15,
    pady=4,
    command=clear_fields
)
btn_clear.pack(pady=5)

# Result Output Label
result_label = tk.Label(
    root, 
    text="", 
    font=("Arial", 14, "bold"), 
    bg="#f0f4f8", 
    fg="#27ae60"
)
result_label.pack(pady=25)

# ── RUN APPLICATION ──────────────────────────────────────────
root.mainloop()