print("Please type in integer numbers. Type in 0 to finish.")

count = 0
add = 0
pos = 0
neg = 0
while True:
    num = int(input("Number:"))
    if num != 0:
        if num > 0:
            pos += 1
        else:
            neg += 1
        count += 1
        add += num
    else:
        break
print("... the program asks for numbers")
print("Numbers typed in", count)
print("The sum of the numbers is", add)
print("The mean of the numbers is", (add/count))
print("Positive numbers", pos)
print("Negative numbers", neg)