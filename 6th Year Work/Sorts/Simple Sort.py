#Author: Vira Ustymenko
#Date: 10th September, 2026
#Description: Simple Sort

L=[2,5,4,10,3,7] #<-- given list, unsorted
M=[] #<-- empty list

var = len(L)
while L:
    small = L[0]
    if len(L)==1:
        pass
    else:
        for i in range(var):
            if small>L[i]:
                small = L[i]
        var -=1
    L.pop(L.index(small)) #<-- moving the smallest number to the list
    M.append(small)      #-----^

print(L,M)
