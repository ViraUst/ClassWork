#Author: Vira Ustymenko
#Date: 21st October 2025
#Description: calculates length of a string through while and for loop

#i)
letter = 0
word = input("Enter word: ")
for i in word:
    letter = letter+1
print("length: ", letter)

#ii)
counting = 0
while counting < len(word):
    counting = counting+1
print("length: ", counting)