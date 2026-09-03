#Author: Vira Ustymenko
#Date: 3rd September
#Description: Binary Search

choice = input("Use 1) Existing list; 2) New list (1/2): ")

if choice == '1':
    L1 = [2,5,8,12,16,56,23,72,38,91]
elif choice == '2':
    L1 = []
    print("Enter list elements. When done enter 'd'")
    a = False
    while a!=True:
        a = input("Enter list element: ")
        if a.lower() == 'd':
            break
        L1.append(int(a))

print("List = ", L1)

L1.sort()

Search = int(input("Which value do you need to find? "))

low = 0
high = len(L1) - 1
middle = (high-low)//2
var = True

if L1[high]<Search:
        index = -1
        var = False

while var:
    if Search > L1[middle]:
        low = middle +1
        middle = (low+high)//2
    elif L1[middle] == Search:
        index = middle
        var = False
    else:
        high = middle-1
        middle = (low+high)//2
    if high == middle:
        index = -1
        var = False

print(index)