'''
Description: Day5 if statement
Version: 0.1
Author: Roy
'''

# Q1: 百分制成绩转换为等级制成绩。
# Hint:
# if score >= 90      , output A.
# if 80 <= score < 90 , output B. 
# if 70 <= score < 80 , output C.
# if 60 <= score < 70 , output D.
# if 60 < score       , output E.

score = float(input("Enter your score value: "))
if score >= 90:
    print("Your grad is A")
elif 80 <= score < 90:
    print("Your grad is B")
elif 70 <= score < 80:
    print("Your grad is C")
elif 60 <= score < 70:
    print("Your grad is D")
else:
    print("Your grad is E")