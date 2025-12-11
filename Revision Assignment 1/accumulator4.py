#Author: Vira Ustymenko
#Date: 8th December 2025
#Description: Program sums all the even numbers between 1
# and 50

integ = 0

for i in range(1,51):
    if i%2==0:
        integ=integ+i

print(integ)
