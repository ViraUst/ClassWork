#Author: Vira Ustymenko
#Date: 10th February, 2026
#Description:import random exercise 2

import random

print("Welcome to my dice game!!")
Name = input("Please enter your name: ")
name = Name+"'s"
lucky_number = int(input("Please select a lucky number between 1 and 6: "))
computer_die_roll = random.randint(1,6)
#^-- initialize computer number
print(name,"lucky number was", lucky_number)
print("The computer rolled: ", computer_die_roll)

if lucky_number == computer_die_roll:
    print("You guessed correclty, well done!")
elif lucky_number < computer_die_roll:
    print("You guessed too low.")
elif lucky_number > computer_die_roll:
    print("You guessed too high.")