# Please write a program which asks the user for four numbers. The program then prints out the sum and the mean of the numbers.

num1 = int(input("Number 1:"))
num2 = int(input("Number 2:"))
num3 = int(input("Number 3:"))
num4 = int(input("Number 4:"))
sum = num1 + num2 + num3 + num4
mean = sum / 4
print(f"The sum of the numbers is {sum} and the mean is {mean}")