#Author: Vira Ustymenko
#Date: 2nd September 2026
#Description: Linear search

answer = True
L1 = []
print("Please enter elements of a list, when finished enter 'f'")
while answer is not False:
    el = input("Enter element: ")
    if el == 'f':
        answer = False
        break
    else:
        L1.append(el)

find = input("Enter element you wish to find: ")
ind = 0
iF = False
for i in L1:
    if i == find:
        iF = True
        print(ind)
        break
    else:
        ind += 1
if iF == False:
    print(-1)