print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? $"))
tip_percentage = int(
    input("What percentage tip would you like to give? 10, 12 or 15? "))
people_quantity = int(input("How many people to split the bill? "))

total_to_people = (total_bill / people_quantity) * \
    ((tip_percentage + 100) / 100)
rounded_total = round(total_to_people, 2)

print(f"Each people should pay: ${rounded_total}")
