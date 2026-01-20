#Author: Vira Ustymenko
#Date: 19th January 2026
#Description: Rotates the elements of a list so that the element at the first index moves to the
#second index, the element in the second index moves to the third, etc., and the element  in the
#last index moves to the first index.

First = [1,2,3,4,5]
print("Original list: ",First)
one = First[len(First)-1]
First.pop(len(First)-1)
First.insert(0,one)
print("Rearranged list: ",First)