#Author: Vira Ustymenko
#Date: 9th September, 2026
#Description: Simple Sort

L=[2,5,4] #<-- given list, unsorted
M=[] #<-- empty list

var = len(L)
while L:
    small = L[0]
    if len(L)==1:
        pass
    else:
        var -=1
        one = 0
        two = 1
        for i in range(var):
            if small>L[two]:
                small = L[two]
            one+=1
            two+=1
    L.pop(L.index(small))
    M.append(small)
print(L,M)
