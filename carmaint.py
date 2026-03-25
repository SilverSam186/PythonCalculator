# Welcome message
print("Welcome to the Car Check System!")
print("We will check if your car is good to go or needs to go to the maintenance company.\n")

# User inputs
brand = input("What Brand is it? ").lower()
production_year = float(input("What is its year of production? "))
car_status = "Not Defined"

# Check car status
if production_year < 2002:
    if brand == "toyota":
        car_status = "Sorry, your Toyota needs maintenance. Please take it to Raylay Car Maintenance."
    elif brand == "honda":
        car_status = "Sorry, your Honda needs maintenance. Please take it to Raylay Car Maintenance."
    elif brand == "bmw":
        car_status = "Sorry, your BMW needs maintenance. Please take it to Raylay Car Maintenance."
    elif brand == "highlander":
        car_status = "Sorry, your HighLander needs maintenance. Please take it to Raylay Car Maintenance."
    elif brand == "volkswagen":
        car_status = "Sorry, your volkswagen needs maintenance. Please take it to Raylay Car Maintenance."
    
    else:
        car_status = f"Sorry, your {brand.capitalize()} needs maintenance. Please take it to Raylay Car Maintenance."

elif production_year <= 2020:  # cars between 2002 and 2020
    if brand == "toyota":
        car_status = "Nice Toyota! You are on the good list so you are free to drive around. Thank you for your time."
    elif brand == "honda":
        car_status = "Nice Honda! You are on the good list so you are free to drive around. Thank you for your time."
    elif brand == "bmw":
        car_status = "Nice BMW! You are on the good list so you are free to drive around. Thank you for your time."
    elif brand == "highlander":
        car_status = "Nice HighLander! You are on the good list so you are free to drive around. Thank you for your time."
    elif brand == "volkswagen":
        car_status = "Nice VolksWagen! You are on the good list so you are free to drive around. Thank you for your time."
    
    else:
        car_status = f"Nice {brand.capitalize()}! You are on the good list so you are free to drive around. Thank you for your time."

elif production_year > 2020:  # cars newer than 2020
    car_status = f"Wow! Your {brand.capitalize()} from {int(production_year)} is super new! You are free to drive around. Thank you for your time."

# Output the result
print("\n" + car_status)


