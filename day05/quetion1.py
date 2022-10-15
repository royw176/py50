'''
Description: Day5- if statement
Version: 0.1
Author: Roy
'''

# Q1: 英制单位英寸与公制单位厘米互换。
# Hint function: 1 inch = 2.54 cm

unit = input("Enter the unit (inch or cm): ")
value = float(input("Enter the value: "))

if unit == "inch":
    print("%.2f inch is %.2f cm : " %(value, value*2.54))
elif unit == "cm":
    print("%.2f cm is %.2f inch : " %(value, value/2.54))
else:
    print("Please enter inch or cm!")

# Extend issue: How to check the value is digital?