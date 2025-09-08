#Author: Vira Ustymenko
#Date: 08th September 2025
#Description: Program asks user for their name and number, displays each letter of
#their name on separate line for the given num. of times

userName = input('Enter your name: ')
userNumber = int(input('Enter a number: '))
for number in range(userNumber):
    for letter in userName:
        print(letter)
    