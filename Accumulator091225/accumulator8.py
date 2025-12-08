#Author: Vira Ustymenko
#Date: 12th December 2025
#Description: Program outputs product of the numbers divisible
# by 5 between 1 and 50

integ = 1

for i in range(1,51):
    if i%5==0:
        integ = integ*i
print(integ)