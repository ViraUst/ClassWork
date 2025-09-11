#Author: Vira Ustymenko
#Date: 09th September 2025
#Description: Prints the total number of digits in a number

given = input('Enter a number: ')
#print(len(given))
#line above: alternate code without the 'for' loop
count = 0
for digit in given:
    count = count + 1
    print(count)