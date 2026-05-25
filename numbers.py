# Please write a program which asks the user for a number. The program then prints out all integer numbers greater than zero but smaller than the input.

num = int(input("Upper limit:"))
start = 1
while start < num:
    print(start)
    start += 1