#Author: Vira Ustymenko
#Date: 5th November, 2026
#Description: Recursive function to get the sum of odd numbers but not including n


def g(n):
    if n == 0:
        return 0
    elif n%2==0:
        return g(n-1)
    else:
        return g(n-1)+n

number = 5
x = g(number-1)
print(x)