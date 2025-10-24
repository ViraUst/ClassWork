#Author: Vira Ustymenko
#Date: 23st October 2025
#Description: adds all numbers in a given string of characters
theSum = 0
tree = input("Enter a string of characters: ")
for t in tree:
    if t in '1234567890':
        t = int(t)
        theSum = t + theSum
    else:
        pass
print('The sum = ', theSum)