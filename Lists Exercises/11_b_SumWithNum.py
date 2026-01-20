#Author: Vira Ustymenko
#Date: 19th January 2026
#Description: (b) L is a list of numbers. Prints a new list where each element is the corresponding
#element of list L summed with number num.

num = float(input("Enter a number: "))
L = [1,2,3,4,5]
New = []
for i in L:
    n = i+num
    New.append(n)
print(New)