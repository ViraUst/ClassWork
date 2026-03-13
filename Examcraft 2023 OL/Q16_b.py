#Author: Vira Ustymenko
#Date: 13th March 2026

#Question 16(b)
import random

words = ["cat","mat","can","man","pool","tool","mule","pat","tan","rule"]
print("The list of words is: ", words)
random_word = words[random.randint(0,len(words)-1)]
print("The length of the word is:",len(random_word))
print("The first letter of the word is:",random_word[0])
guess = input("Please guess what the word is: ")


if guess == random_word:
    print("You guessed correctly!")

else:
    print("Incorrect, try again.")
    
    for i in range(2):
        guess2 = input("Please, take another guess: ")
        if guess2 == random_word:
            print("You guessed correctly!")
            break
        print("Incorrect, try again.")

print("The word was:", random_word)