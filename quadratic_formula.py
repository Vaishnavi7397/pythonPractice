# Please write a program for solving a quadratic equation of the form ax²+bx+c. The program asks for values a, b and c. It should then use the quadratic formula to solve the equation. The quadratic formula expressed with the Python sqrt function is as follows:

# x = (-b ± sqrt(b²-4ac))/(2a).

# You can assume the equation will always have two real roots, so the above formula will always work.

from math import sqrt
a = float(input("Value of a:"))
b = float(input("Value of b:"))
c = float(input("Value of c:"))

x1 = float((-b + sqrt(b**2 - 4*a*c))/(2*a))
x2 = float((-b - sqrt(b**2 - 4*a*c))/(2*a))

print("The roots are", x1, "and", x2)