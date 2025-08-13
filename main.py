from tkinter import *
import tkinter as tk

from tkinter import messagebox

def fahrenheit_to_celsius():
    try:
        fahrenheit = float(entry_fahrenheit.get())
        celsius = (fahrenheit - 32) * 5/9
        label_result.config(text=f"{celsius:.2f} °C")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number")

# Create main window
window = tk.Tk()
window.title("Temperature Converter")
window.geometry("300x150")
window.resizable(False, False)

# Create and pack widgets
label_instruction = tk.Label(window, text="Enter temperature in Fahrenheit:")
label_instruction.pack(pady=10)

entry_fahrenheit = tk.Entry(window, width=10)
entry_fahrenheit.pack()

button_convert = tk.Button(window, text="Convert to Celsius", command=fahrenheit_to_celsius)
button_convert.pack(pady=10)

label_result = tk.Label(window, text="Result will appear here")
label_result.pack(pady=10)

# Start the main loop
window.mainloop()

