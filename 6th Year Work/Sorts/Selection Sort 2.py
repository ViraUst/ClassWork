#Author: Vira Ustymenko
#Date: 9th September
#Description: Selection Sort by pseudo-code from the task


array = [3,5,2,7,1]

size = len(array)
for i in range(0,size-1):
    minim = i
    for j in range(i+1,size):
        if array[j]<array[minim]:
            minim = j
    if minim!=i:
        swap = array[i]
        array[i] = array[minim]
        array[minim] = swap
print(array)