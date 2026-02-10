#Author: Vira Ustymenko
#Date: 9th February, 2026
#Description: Randomly chooses Heads or Tails, asks user for input displays if the input is equal to the random value, shows both
#user input and the random value

import random

HT = ['Heads','Tails']
user = input("Enter either Heads or Tails: ")
randHT = random.choice(HT)

if randHT == user:
    print("You win!")
else:
    print("You lose.")

print("The random is: ", randHT)
print("Your input was: ", user)