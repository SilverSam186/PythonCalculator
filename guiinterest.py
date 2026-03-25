# Welcome Message
print("Welcome to Sam's Interest Calculator\n")
print("Let's help you out")

import tkinter as tk

window = tk.Tk()
window.title("Stage 2 Practice")

tk.Label(window, text="Your Name").grid(row=0, column=0)
name_entry = tk.Entry(window)
name_entry.grid(row=0, column=1)

def show_name():
    print(name_entry.get())

tk.Button(window, text="Show", command=show_name).grid(row=1, column=0, columnspan=2)

window.mainloop()

#function for Input
def enterInput(labeL: str):
    while True:
        # get input value
        property = input("Enter the "+labeL+": ")

        # is the value empty 
        if not property.strip():
            print("↪ Invalid Input. ["+labeL+"] required")
        else:
            # check if value is a number
            try:
                # this is where you run your try code
                float(property)
                break
            except Exception as e:
                # if an error occurs
                print("↪ Invalid Input. Digits only")
    return property

def format_money(value, symbol):
    if value is None:
        return "N/A"
    return f"{symbol}{value:,.2f}"

#Ask the user what they want to find

print("\nWhat do you want to calculate?")
print("1. Simple Interest")
print("2. Principal")
print("3. Rate Percent")
print("4. Time (years)")

choice = input("Enter the number of your choice: ")

principal_input = None
rate_percent_input = None
time_input = None
simple_interest_input = None

if choice == "1":
    principal_input = enterInput("Principal")
    rate_percent_input = enterInput("Rate Percent")
    time_input = enterInput("Time (in years)")

elif choice == "2":
    simple_interest_input = enterInput("Simple Interest")
    rate_percent_input = enterInput("Rate Percent")
    time_input = enterInput("Time (in years)")

elif choice == "3":
    simple_interest_input = enterInput("Simple Interest")
    principal_input = enterInput("Principal")
    time_input = enterInput("Time (in years)")

elif choice == "4":
    simple_interest_input = enterInput("Simple Interest")
    principal_input = enterInput("Principal")
    rate_percent_input = enterInput("Rate Percent")

else:
    print("Invalid choice.")
    exit()

# Step 2: Convert to float

principal = float(principal_input) if principal_input else None
rate_percent = float(rate_percent_input) if rate_percent_input else None
time = float(time_input) if time_input else None
simple_interest = float(simple_interest_input) if simple_interest_input else None

rate = rate_percent / 100 if rate_percent is not None else None

# Step 3: Choose Currency

print("\nChoose currency:")
print("1. Naira (₦)")
print("2. Dollar ($)")
print("3. Pound (£)")

currency_choice = input("Enter choice: ")

if currency_choice == "1":
    currency = "₦"
elif currency_choice == "2":
    currency = "$"
elif currency_choice == "3":
    currency = "£"
else:
    currency = "₦"  # default

#Calculation

print("\n=== RESULT ===")

if simple_interest is None:
    if isinstance(principal, float) and isinstance(rate, float) and isinstance(time, float):
        simple_interest = principal * rate * time
        total = principal + simple_interest
        print("Simple Interest:", format_money(simple_interest, currency))
        print("Total Amount to Pay:", format_money(total, currency))

elif principal is None:
    if isinstance(rate, float) and isinstance(time, float):
        principal = simple_interest / (rate * time)
        print("Principal:", format_money(principal, currency))

elif rate is None:
    if isinstance(principal, float) and isinstance(time, float):
        rate = simple_interest / (principal * time)
        print("Rate Percent:", f"{rate * 100:.2f}%")

elif time is None:
    time = simple_interest / (principal * rate)
    print("Time (years):", f"{time:.2f}")

# =========================
# Step 5: Explanation
# =========================

print("\nWant to know how we did it?")
print("1. Yes")
print("2. No")

explain_choice = input("Enter choice: ")

if explain_choice == "1":
    print("\n=== EXPLANATION ===")

    if choice == "1":
        print("Formula:")
        print("Simple Interest = Principal × Rate × Time\n")
        print(f"= {principal} × {rate} × {time}")
        print("Simple Interest =", format_money(simple_interest, currency))

    elif choice == "2":
        print("Formula:")
        print("Principal = Simple Interest ÷ (Rate × Time)\n")
        print(f"= {simple_interest} ÷ ({rate} × {time})")
        print("Principal =", format_money(principal, currency))

    elif choice == "3":
        if isinstance(rate, float):
            print("Formula:")
            print("Rate = Simple Interest ÷ (Principal × Time)\n")
            print(f"= {simple_interest} ÷ ({principal} × {time})")
            print(f"Rate Percent = {rate * 100:.2f}%")

    elif choice == "4":
        print("Formula:")
        print("Time = Simple Interest ÷ (Principal × Rate)\n")
        print(f"= {simple_interest} ÷ ({principal} × {rate})")
        print(f"Time = {time:.2f} years")

else:
    print("Thank you for choosing us!")

print("\nThank you for using Sam's Interest Calculator 👋")
