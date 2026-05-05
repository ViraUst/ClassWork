#Author: Vira Ustymenko
#Date: 30th April 2026
#Description: function returns the lesser of two numbers if both are even, if
#one or both are odd returns the greater

def two_events(a,b):
    numbers = [a,b]
    if a%2==0 and b%2==0:
        result = min(numbers)
    else:
        result = max(numbers)
    return result

x = two_events(2,4)
y = two_events(2,5)
print(x,y)