# Please write a program which estimates a user's typical food expenditure.

# The program asks the user how many times a week they eat at the student cafeteria. Then it asks for the price of a typical student lunch, and for money spent on groceries during the week.

# Based on this information the program calculates the user's typical food expenditure both weekly and daily.

# The program should function as follows:

# Sample output
# How many times a week do you eat at the student cafeteria? 4
# The price of a typical student lunch? 2.5
# How much money do you spend on groceries in a week? 28.5

# Average food expenditure:
# Daily: 5.5 euros
# Weekly: 38.5 euros

days = int(input("How many times a week do you eat at the student cafeteria?"))
lunch_price = float(input("The price of a typical student lunch?"))
Total_lunch_price = days*lunch_price
Weekly_groceries_expenditure = float(input("How much money do you spend on groceries in a week?"))

Weekly_expenditure = Total_lunch_price + Weekly_groceries_expenditure
daily_expenditure = Weekly_expenditure/7

print()
print("Average food expenditure:")
print(f"Daily: {daily_expenditure} euros")
print(f"Weekly: {Weekly_expenditure} euros") 