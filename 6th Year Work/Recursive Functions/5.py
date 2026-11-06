#Author: Vira Ustymenko
#Date: 6th November, 2026
#Description: Recursive function to get the sum of the reciprocal of the first n positive integers

def f(n):
    if n ==1:
        return 1
    else:
        return 1/n+f(n-1)
number = 2
x = f(number)
print(x)