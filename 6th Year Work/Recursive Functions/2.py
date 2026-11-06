#Author: Vira Ustymenko
#Date: 5th November, 2026
#Description: Recursive function to calculate the num of characters in a string



def gee(chara):
    if len(chara)==0:
        return 0
    else:
        return gee(chara[1:])+1

lisT = "hello"
x = gee(lisT)
print(x)