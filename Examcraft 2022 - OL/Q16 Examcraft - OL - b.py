#Author: Vira Ustymenko
#Date: 12th March 2026
#Question 16 b

import random

computer_options = ['rock','paper','scissors']

computer_choice = computer_options[random.randint(0,2)]

player_c = input("Enter rock, paper or scissors: ")
print("Player chose: ",player_c)
print("The computer chose: ",computer_choice)

if player_c == computer_choice:
    print("Draw!")
elif player_c == "scissors":
    if computer_choice == "paper":
        print("Player wins")
    elif computer_choice == "rock":
        print("Computer wins")
elif player_c == "paper":
    if computer_choice == "rock":
        print("Player wins")
    elif computer_choice == "scissors":
        print("Computer wins")
elif player_c == "rock":
    if computer_choice == "scissors":
        print("Player wins")
    elif computer_choice == "paper":
        print("Computer wins")