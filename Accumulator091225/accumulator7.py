#Author: Vira Ustymenko
#Date: 12th December 2025
#Description: Program outputs product of the even numbers
# between 1 and 50

integ = 1

for i in range(1,51):
    if i%2==0:
        integ = integ*i
print(integ)