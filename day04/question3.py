'''
Description: Day4-symbol of operation
Version: 0.1
Author: Roy
'''

# Q3: Determining whether it is a leap year?
# Enter the year, if it is leap year, output true. If it is not, output false.
# Hint1: 可以被4整除，且不被100整除。
# Hint2: 可被400整除。
# Hint3: 可被1000整除。

year = int(input("Enter the year: "))
leap = year % 4 == 0 or year % 400 == 0 and year % 100 != 0
print("year is leap year? A = " , leap)