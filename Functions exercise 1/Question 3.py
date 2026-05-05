#Author: Vira Ustymenko
#Date: 30th April 2026
#Description: given two integers function returns True if the sum of the integers is 20 or one of the integers
# is 20. If not, returns False

def makes_twenty(a,b):
    if a==20 or b==20 or a+b == 20:
        heh = True
    else:
        heh = False
    return heh

x = makes_twenty(20,10)
y = makes_twenty(12,8)
z = makes_twenty(2,3)
print(x,y,z)