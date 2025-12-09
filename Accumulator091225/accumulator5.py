#Author: Vira Ustymenko
#Date: 8th December 2025
#Description: Program sums all the odd numbers between 1
# and value entered by user

integ = 0
val = int(input("Enter end number: "))

for i in range(1,(val+1)):
    if i%2!=0:
        integ=integ+i

print(integ)
