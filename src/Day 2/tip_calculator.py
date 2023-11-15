print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
people = int(input("How many people to split the bill? "))
tip = float(input("What percentage tip you want to give? 10%, 12% or 15%? "))

individual_bill = round((bill*(1 + tip/100))/people, 2)

print(f"Each person should pay: ${individual_bill}")