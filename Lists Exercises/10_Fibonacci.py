#Author: Vira Ustymenko
#Date: 19th January 2026
#Description: Program reads the n to display nth term of Fibonacci series

n = int(input("Enter a number (under 20): "))

one = 0
two = 1

for i in range(n-1):
    three = one+two
    one = two
    two = three

if n == 1:
    print(0)
else:
    print(two)