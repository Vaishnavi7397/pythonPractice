# Please write a program which asks the user for a year, and prints out the next leap year.
org_year = int(input("Year:"))
year = org_year + 1

while True:
    if year % 100 == 0:
        if year % 400 == 0:
            break
    elif year % 4 == 0:
        break

    year += 1

print(f"The next leap year after {org_year} is {year}")
