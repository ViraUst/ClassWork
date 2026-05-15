#Author: Vira Ustymenko
#Date: 15th May 2026
#Description: Question 6 with feedback changes

def almost_there(n):
    if (n >= 100 and n<=110) or (n <=100 and n>=90) or (n>=200 and n<=210) or (n<=200 and n>=190):
        result = True
    else:
        result = False
    return result

w = almost_there(90)
x = almost_there(104)
y = almost_there(150)
z = almost_there(193)

print(w,x,y,z)
