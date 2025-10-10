#Author: Vira Ustymenko
#Date: 9th October 2025
#Description: sums 7 terms of a sequence (a) -  2/9-5/13+8/17

add = 0
addtoo = 0
top = 2
bottom = 9
num = 0
total = 0
while num! = 7:
    top=top+add
    if top%2==0:
        bottom=bottom+addtoo
    else:
        bottom=(bottom+addtoo)*-1
    seq=top/bottom
    add = 3
    addtoo = 4
    num = num+1
    total= total+seq
    print(seq)
print(total)