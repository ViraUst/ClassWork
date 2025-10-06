#Author: Vira Ustymenko
#Date: 03 October 2025
#Description: Program prints from 1 to n using a while loop, skips every multiple
# of 5
random = 1
n = int(input("Enter an integer number: "))
while random<=n:
    if random%5 == 0:
        pass
    else:
        print(random, end=' ')
    random = random + 1