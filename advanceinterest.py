#Welcome Message
print("Welcome to Sam's Interest Calculator\n")
print("Let's help you out")

# Step 1: Ask the user what they want to find
print("What do you want to calculate?")
print("1. Simple Interest")
print("2. Principal")
print("3. Rate Percent")
print("4. Time (years)")

choice = input("Enter the number of your choice: ")
choices = ("Simple Interest", "Principal", "Rate Percent", "Time")

# Step 2: User Inputs
principal_input = None
rate_percent_input = None
time_input = None
simple_interest_input = None

# function for input
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

# end of function


if choice == "1":  # Find Simple Interest
    principal_input = enterInput("Principal")
    rate_percent_input = enterInput("Rate Percent")
    time_input = enterInput("Time (in years)")

elif choice == "2":  # Find Principal
    simple_interest_input = enterInput("Simple Interest")
    rate_percent_input = enterInput("Rate Percent")
    time_input = enterInput("Time (in years)")

elif choice == "3":  # Find Rate Percent
    simple_interest_input = enterInput("Simple Interest")
    principal_input = enterInput("Principal")
    time_input = enterInput("Time (in years)")

elif choice == "4":  # Find Time
    simple_interest_input = enterInput("Simple Interest")
    principal_input = enterInput("Principal")
    rate_percent_input = enterInput("Rate Percent")

else:
    print("Invalid choice. Please select an option 1, 2, 3, or 4.")
    exit()

# CHECK IF VALID


# Step 3: Convert inputs to float
principal = float(principal_input) if principal_input else None
rate_percent = float(rate_percent_input) if rate_percent_input else None
time = float(time_input) if time_input else None
simple_interest = float(simple_interest_input) if simple_interest_input else None

# Step 4: Convert rate percent to decimal
rate = rate_percent / 100 if rate_percent is not None else None


print("\n=== RESULT ===")

# Step 5: Perform calculation based on what was missing
if simple_interest is None:
    if isinstance(principal, float) and isinstance(rate, float) and isinstance(time, float):
        simple_interest = principal * rate * time
        print("Simple Interest:", simple_interest)
        print("Total Amount to Pay:", principal + simple_interest)

elif principal is None:
    if isinstance(rate, float) and isinstance(time, float):
        principal = simple_interest / (rate * time)
        print("Principal:", principal)

elif rate is None:
    if isinstance(principal, float) and isinstance(time, float):
        rate = simple_interest / (principal * time)
        print("Rate Percent:", rate * 100)

elif time is None:
    time = simple_interest / (principal * rate)
    print("Time (years):", time)

print("Thank you for choosing us till next time Bye")


# Ask
print("\nWant to know how we did it?")
print("1. Yes")
print("2. No")

explain_choice = enterInput("Enter the number of your choice: ")

if explain_choice == "1":
    print("\nWhat would you like to know?")
    print("1. Simple Interest")
    print("2. Principal")
    print("3. Rate Percent")
    print("4. Time (years)")

    explain_option = enterInput("Enter the number of your choice: ")

    print("\n=== EXPLANATION ===")

    if explain_option == "1":
        print("Formula:")
        print("Simple Interest = Principal × Rate × Time\n")

        print("Substitution:")
        print(f"= {principal} × {rate} × {time}")

        print(f"\nAnswer:")
        print(f"Simple Interest = {simple_interest}")

    elif explain_option == "2":
        print("Formula:")
        print("Principal = Simple Interest ÷ (Rate × Time)\n")

        print("Substitution:")
        print(f"= {simple_interest} ÷ ({rate} × {time})")

        print(f"\nAnswer:")
        print(f"Principal = {principal}")

    elif explain_option == "3":
        if isinstance(rate, float):
            print("Formula:")
            print("Rate = Simple Interest ÷ (Principal × Time)\n")

            print("Substitution:")
            print(f"= {simple_interest} ÷ ({principal} × {time})")

            print(f"\nAnswer:")
            print(f"Rate Percent = {rate * 100}") 

    elif explain_option == "4":
        print("Formula:")
        print("Time = Simple Interest ÷ (Principal × Rate)\n")

        print("Substitution:")
        print(f"= {simple_interest} ÷ ({principal} × {rate})")

        print(f"\nAnswer:")
        print(f"Time = {time} years")

    else:
        print("Invalid choice.")

elif explain_choice == "2":
    print("Thank you for choosing us. Bye for now 👋")

else:
    print("Invalid choice.")

print("\nThank you for choosing Sam's Interest Calculator. Till next time 👋")
print("And for anyone who's name is also Sam you are highly welcome ")
print("For anyone who finds this helpful and wants to know how i did it chat me up in the comment section.")

