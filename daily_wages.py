# Please write a program which asks for the hourly wage, hours worked, and the day of the week. The program should then print out the daily wages, which equal hourly wage multiplied by hours worked, except on Sundays when the hourly wage is doubled.

wage = float(input("Hourly wage:"))
hours = int(input("Hours worked:"))
day = input("Day of the week:")
if(day == "Sunday"):
    print(f"Daily wages: {wage*hours*2} euros")

if day != "Sunday":
    print(f"Daily wages: {wage*hours} euros")