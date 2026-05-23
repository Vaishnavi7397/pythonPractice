# Please write a program which asks the user for a temperature in degrees Fahrenheit, and then prints out the same in degrees Celsius. If the converted temperature falls below zero degrees Celsius, the program should also print out "Brr! It's cold in here!".

# The formula for converting degrees Fahrenheit to degrees Celsius can be found easily by any search engine of your choice.

f = int(input("Please type in a temperature(F):"))
c = ((f-32)*5)/9 
print(f"{f} degrees Fahrenheit equals {c} degrees Celsius")

if c < 0:
    print("Brr! It's cold in here!")