#user inputs
user_name = input("What's your name? ")
user_travel = input("Where are you traveling to? ")
total_miles = input("How many miles is the trip one way? ")
vehicle_mpg = input("How many mpg does your car get? ")
gas_price = input("What is the price of gas per gallon? ")
number_of_travelers = input("How many people are traveling? ")

#convert inputs from string to float
total_miles= float(total_miles)
vehicle_mpg= float(vehicle_mpg)
gas_price = float(gas_price)
number_of_travelers= float(number_of_travelers)


#name variable
gallons= total_miles/vehicle_mpg
gas_total = gas_price*total_miles
per_person = (gas_price*total_miles)/number_of_travelers
#shown on screen 

#header 
print("Travel Summary".upper())

#name and location
print(f"Traveler: {user_name}")
print(f"Destination: {user_travel}")

#gas needed and total cost
print(f"Gallons of gas: {gallons}")
print(f"Total price of gas: ${gas_total}")

#cost per person
print(f"Cost per person: ${per_person}")

#footer
print("Have a fun trip!")

