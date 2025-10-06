#Author: Vira Ustymenko
#Date: 03 October 2025
#Description: Program takes numbers until thier sum is more than 50
count = 0
while count<=50:
    number = float(input("Enter a number: "))
    count = count + number
print(count, '> 50')