#Author: Vira Ustymenko
#Date: 03 October 2025
#Description: program asks user to guess a set value, tells if the input is too high
# or too low, prints a well done message when guessed correctly, and how many
# attempts it took
enigma = 33.5
attempts = 1
while enigma == 33.5:
    guess = float(input("Enter a guess: "))
    if guess==enigma:
        print("You guessed correctly, well done! Go eat sweets.")
        break
    elif guess>enigma:
        print("Oops, too high.")
    elif guess<enigma:
        print("Nah, too low.")
    attempts = attempts + 1

if attempts>1:
    print("Wow, it only took you", attempts, "guesses!")
else:
    print("Wow, it only took you", attempts, "guess!")