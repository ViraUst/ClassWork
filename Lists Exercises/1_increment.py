#Author: Vira Ustymenko
#Date: 15th January 2026
#Description: Write a program to increment the elements of a list with a number

#1) - adds a number element
ls = [1,2,3,4,5]
ls.append(6)
print(ls)

#2) - adds a number to each element
ls = [1,2,3,4,5]
k = []
for i in ls:
    k.append(i+5)
print(k)
