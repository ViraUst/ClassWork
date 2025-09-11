#Author: Vira Ustymenko
#Date: 09th September 2025
#Description: Prints the sum of all the odd numbers from 1 to a given number
variable = 0
Given = int(input('Enter an end range number: '))+1
for the_sum in range(1,Given):
    if the_sum%2 == 1:
        variable = variable + the_sum
print(variable)