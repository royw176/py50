'''
Description: Day4 symbol of operation
Version: 0.1
Author: Roy
'''
# Q2: Enter the radius of the circle to calculate circumference and circle area.
# Hint1: Circumference funciton: Diameter * 3.14
# Hint2: Circle area   function: redius^2 * 3.14
r = float(input("Radius of the circle is: "))
d = float(r + r)
print("Diameter is : %.2f" % d)

cf = float(d * 3.14)
ca = float(r**2 * 3.14)
print("Circumference is : %.2f" % cf)
print("Circle Area is : %.2f" % ca)