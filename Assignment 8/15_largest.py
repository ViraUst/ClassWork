#Author: Vira Ustymenko
#Date: 07th October 2025
#Description: finds largest number of a list of numbers entered through keyboard
number = 8
a = 0
while number != 0:
    number = float(input("Enter a number, to stop enter 0: "))
    if number>a:
        um = number
    a = a + number
print("Largest number: ",um)