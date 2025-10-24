#Author: Vira Ustymenko
#Date: 23st October 2025
#Description: asks user to guess a set number from 1 to 100, tells if answer is too
# high or low, they have only 7 attempts. if they use more than 7 prints 'Game Over'
# and prints the answer

number = 50
tries = 0
while tries <= 7:
    tries = tries + 1
    guess = float(input("Enter a number from 1 to 100:"))
    if guess < number:
        print('Too low')
    elif guess > number:
        print('Too high')
    else:
        print('Well done')
        break
if tries > 7:
    print('Game over, the number was:', number)
