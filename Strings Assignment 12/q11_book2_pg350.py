#Author: Vira Ustymenko
#Date: 4th November 2025
#Description: Program counts an estimated amount of words in a given by user string

stwing = input("Enter a sentence with only single space between words: ")
count = 1
#the initial 1 is for the word at the end, as it will not have a following space.

print("Number of entered words(method1): ", (stwing.count(' ')+1))


for i in stwing:
    if i == ' ':
        count = count+1
    else:
        pass

print("Number of entered words(method2): ",count)