#Author: Vira Ustymenko
#Date: 20th January 2026
#Description: compares two equal sized lists, prints the first index where they differ.

list1 = [3,'abc',53,0,'mango']
list2 = [3,'abc',53,4,'papaya']
print("list1 =", list1, ", list2 =", list2)

index = 0
for l in list1:
    if l == list2[index]:
        pass
        index +=1
    else:
        diff = index
        break
print("First difference in elements at index: ", diff)
