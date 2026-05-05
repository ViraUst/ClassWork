#Author: Vira Ustymenko
#Date: 30th April 2026
#Description: function takes a two-word string and returns True if both words begin with the same letter

def animal_crackers(words):
    letter1 = words[0]
    letter2 = words[words.find(' ')+1]
    if letter1 == letter2:
        result = True
    else:
        result = False
    return result

x = animal_crackers('Levelheaded Llama')
y = animal_crackers('Crazy Kangaroo')
print(x,y)