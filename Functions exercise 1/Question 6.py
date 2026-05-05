#Author: Vira Ustymenko
#Date: 1st May 2026
#Description: Given an integer n, function returns True if n is within 10 of either 100 or 200

def almost_there(n):
    if (n >= 100 and n<=110) or (n <=100 and n>=90) or (n>=200 and n<=210) or (n<=200 and n>=210):
        result = True
    else:
        result = False
    return result

w = almost_there(90)
x = almost_there(104)
y = almost_there(150)
z = almost_there(209)

print(w,x,y,z)
