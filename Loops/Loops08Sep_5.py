#Author: Vira Ustymenko
#Date: 08th September 2025
#Description: Program asks user for 5 numbers, after each input asks if they wish to
# add the num. to the total. If yes, adds it to total, else doesn't. When 5 numbers
# are entered displays total.

total = 0

for loop1 in range(5):
    user_number = int(input('Enter a number: '))
    question = input('Do you wish to add it to the total?(Yes/No): ')
    if question == 'yes' or question == 'Yes':
        total = total + user_number
    else:
        pass
print('Total = ', total)