#Author: Vira Ustymenko
#Date: 5th November, 2026
#Description: Recursive function to calculate a sum of a list



def gee(figures):
    if len(figures)==0:
        return 0
    else:
        return gee(figures[1:])+figures[0]

lisT = [5,2,3,4,6,1]
x = gee(lisT)
print(x)