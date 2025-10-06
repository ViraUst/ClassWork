#Author: Vira Ustymenko
#Date: 03 October 2025
#Description: Program prints from 1 to n squared, stops the loop when iteration
# number is 50.
random = 1
n = int(input("Enter an integer number: "))
n = n**2
while random<=n:
    if random > 50:
        break
    else:
        print(random, end=' ')
    random = random + 1