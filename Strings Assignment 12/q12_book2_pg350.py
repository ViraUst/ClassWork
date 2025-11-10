#Author: Vira Ustymenko
#Date: 4th November 2025
#Description: takes a formula and checks if it has the same number of parentheses

formula = input("Enter a formula: ")
'''Open = 0
Close = 0
for i in formula:
    if i == '(':
        Open = Open+1
    elif i == ')':
        Close = Close + 1
    else:
        pass
    
if Close == Open:
    print("Same number of parentheses")
else:
    print("Not same number of parentheses")''' #for loop way
        

open_1 = formula.count('(')
closed_1 = formula.count(')')


if closed_1 == open_1:
    print("Same number of parentheses")
else:
    print("Not same number of parentheses")
        