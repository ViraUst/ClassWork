#Author: Vira Ustymenko
#Date: 23rd Februrary 2026
#Description: Exercise 3, calculate mean, median, and mode
import math
values = [22,13,28,13,22,25,7,13,25]

mean = sum(values)/len(values)
print("Mean: ",mean)
st = 0
for i in values:
    if values.count(i) > st:
        st = values.count(i)
        mode = i

print("Mode: ",mode)

median = values[math.floor(len(values)/2)]
print("Median: ", median)