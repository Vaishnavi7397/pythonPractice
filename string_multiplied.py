# Please write a program which asks the user for a string and an amount. 
# The program then prints out the string as many times as specified by the amount. 
# The printout should all be on one line, with no extra spaces or symbols added.

word = input("Please type in a sring:")
amt = int(input("Please type in an amount:"))
start = 0
string = ""
while start < amt:
    string += word
    start += 1
print(string)