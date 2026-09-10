#Author: Vira Ustymenko
#Date: 2nd September 2026
#Description: Linear search

answer = True
L1 = []
print("Please enter elements of a list, when finished enter 'f'")
while answer:
    el = input("Enter element: ")
    if el.lower() == 'f':
        answer = False
    else:
        L1.append(el)
print("Your list:", L1)

find = input("Enter element you wish to find: ")
ind = 0
for i in L1:
    if i == find:
        answer = True
        print(ind)
        break
    else:
        ind += 1
if answer == False:
    print(-1)
