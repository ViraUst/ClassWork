#Author: Vira Ustymenko
#Date: 12th December 2025
#Description: Program sums the first n integers entered by
# the user

integer = 0
many = int(input("Enter a number of integers to be summed: "))

for i in range(1,(many+1)):
    integer = integer + i
print(integer)