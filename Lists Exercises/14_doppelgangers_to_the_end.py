#Author: Vira Ustymenko
#Date: 20th January 2026
#Description: moves all duplicate values in a list to the end of the list.

bones = [3,3,3,7,77,8,8,0,19]

for i in bones:
    amount = bones.count(i)
    if amount > 1:
        for k in range(amount):
            bones.remove(i)
            bones.append(i)
print(bones)