#Author: Vira Ustymenko
#Date: 5th May 2026
#Description: Function returns the sum of numbers in the array, except ignores sections of numbers starting
# with a 6 extending to the next 9(every 6 will be followed by at least one nine). Returns 0 for no numbers

def summer_69(key):
    suma = 0
    ghost = False
    for i in key:
        if i == 6:
            ghost=True
        if ghost == True and i == 9:
            i = 0
            ghost=False
        if ghost == True:
            i = 0
        suma += i
    return suma
x = summer_69([1,3,5])
y = summer_69([4,5,6,7,8,9])
z = summer_69([2,1,6,9,11])
print(x,y,z)