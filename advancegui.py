import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Sam's Interest Calculator")
window.geometry("400x400")
window.resizable(False, False)

# =========================
# Currency Input
tk.Label(window, text="Currency Symbol:").grid(row=6, column=0, padx=10, pady=5, sticky="e")
currency_entry = tk.Entry(window)
currency_entry.grid(row=6, column=1, padx=10, pady=5)
currency_entry.insert(0, "₦")  # Default currency

# =========================
# Labels and Inputs
tk.Label(window, text="Principal").grid(row=0, column=0, padx=10, pady=5, sticky="e")
tk.Label(window, text="Rate (%)").grid(row=1, column=0, padx=10, pady=5, sticky="e")
tk.Label(window, text="Time (in years)").grid(row=2, column=0, padx=10, pady=5, sticky="e")

principal_entry = tk.Entry(window)
principal_entry.grid(row=0, column=1, padx=10, pady=5)
rate_entry = tk.Entry(window)
rate_entry.grid(row=1, column=1, padx=10, pady=5)
time_entry = tk.Entry(window)
time_entry.grid(row=2, column=1, padx=10, pady=5)

# Dropdown
tk.Label(window, text="Find:").grid(row=3, column=0, padx=10, pady=5, sticky="e")
dropdown = ttk.Combobox(window, values=["SI", "P", "R", "T"])
dropdown.grid(row=3, column=1, padx=10, pady=5)
dropdown.current(0)

# =========================
# Label to show result
result_label = tk.Label(window, text="", justify="left")
result_label.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

# =========================
# Functions
def calculate():
    try:
        principal = float(principal_entry.get())
        rate = float(rate_entry.get()) / 100
        time = float(time_entry.get())
        choice = dropdown.get()
        currency = currency_entry.get()  # get the symbol from user

        if choice == "SI":
            si = principal * rate * time
            total = principal + si
            # Show results with commas and currency
            result_label.config(
                text=f"Principal: {currency}{principal:,.2f}\n"
                     f"Rate: {rate*100:.2f}%\n"
                     f"Time: {time:.2f} years\n"
                     f"Simple Interest: {currency}{si:,.2f}\n"
                     f"Total Amount: {currency}{total:,.2f}"
            )
        else:
            result_label.config(text="Calculation not implemented yet")
    except ValueError:
        result_label.config(text="Please enter valid numbers")

# =========================
# Button
calc_button = tk.Button(window, text="Calculate", command=calculate)
calc_button.grid(row=4, column=0, columnspan=2, pady=10)

window.mainloop()
