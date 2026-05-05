#Author: Vira Ustymenko
#Date: 1st May 2026
#Description: function given a list if ints returns True if the array contains a 3 next to a 3 somewhere

def has_33(beep):
    boop = str(beep)
    if '3, 3' in boop:
        result = True
    else:
        result = False
    return result
x = has_33([1,3,3])
y = has_33([1,3,1,3])
z = has_33([3,1,3])
print(x,y,z)