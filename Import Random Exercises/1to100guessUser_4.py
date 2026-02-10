#Author: Vira Ustymenko
#Date: 9th February, 2026
#Description: chooses a random number between 1 and 100, asks for user input, can keep guessing until the user guesses correctly,
#or they use up 7 turns

import random

turns = 7
randNum = random.randint(1,100)
win = False
while turns:
    user = input("Guess a number from 1 to 100: ")
    if int(user) == randNum:
        win == True
        break
    elif not turns == 1:
        print("Incorrect, try again.")
    turns -=1

if win:
    print("Well done, you guessed correctly!")
else:
    print("You've run out of turns. The number was: ", randNum)