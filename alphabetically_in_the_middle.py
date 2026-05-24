# Please write a program which asks the user for three letters. 
# The program should then print out whichever of the three letters would be in the middle if the letters were in alphabetical order.

# You may assume the letters will be either all uppercase, or all lowercase.

let1 = input("1st letter:")
let2 = input("2nd letter:")
let3 = input("3rd letter:")
if let1 > let2 and let1 > let3:
    if let2 > let3:
        print("The letter in the middle is", let2)
    else:
        print("The letter in the middle is", let3)
elif let2 > let3:
    if let1 > let3:
        print("The letter in the middle is", let1)
    else:
        print("The letter in the middle is", let3)
else:
    if let1 > let2:
        print("The letter in the middle is", let1)
    else:
        print("The letter in the middle is", let2)