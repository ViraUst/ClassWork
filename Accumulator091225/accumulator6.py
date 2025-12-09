#Author: Vira Ustymenko
#Date: 8th December 2025
#Description: Program sums all the multiples of 3 between
# 1 and 50

integ = 0
val = 51

for i in range(1,val):
    if i%3==0:
        integ=integ+i

print(integ)
