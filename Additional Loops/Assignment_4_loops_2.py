#Author: Vira Ustymenko
#Date: 09th September 2025
#Description: Prints all the even numbers within a given range

RangeStart = int(input('Enter the start number of the range: '))
RangeEnd = int(input('Enter the end number of the range: '))

for numbers in range(RangeStart,RangeEnd):
    if numbers%2 == 0:
        print(numbers)
    else:
        pass