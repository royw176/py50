'''
Description: Day5 if statement
Version: 0.1
Author: Roy
'''

# Q1: Enter side length of triangle to calculate triangle perimeter and triangle area.
# Hint1: 三角形任意兩邊的和大於第三邊，任意兩邊的差小於第三邊。
# Hint2: triangle perimeter function: tp = a + b + c
# Hint3: triangle area      function: s = tp / 2 ; ta = (s(s-a)(s-b)(s-c))**0.5
a = float(input("Enter the side length a = "))
b = float(input("Enter the side length b = "))
c = float(input("Enter the side length c = "))


if (a + b > c and a + c > b and b + c > a) or (a - c < b and a - b < c and b - c < a and c - a < b and b - a and c and c - b < a):
    tp = a + b + c
    print("triangle perimeter is %.2f" %tp)
    s = tp / 2
    ta = (s*(s-a)*(s-b)*(s-c))**0.5
    print("triangle area is %.2f" %ta)
else:
    print("Cannot become to triangle.")

# Ref doc: http://www2.chsh.chc.edu.tw/bee/1050206/heron%20formula.pdf
# Ref doc: https://www.ehanlin.com.tw/app/keyword/%E5%9C%8B%E4%B8%AD/%E6%95%B8%E5%AD%B8/%E4%B8%89%E8%A7%92%E5%BD%A2%E4%B8%89%E9%82%8A%E9%95%B7%E7%9A%84%E9%97%9C%E4%BF%82.html