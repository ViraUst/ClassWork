#Author: Vira Ustymenko
#Date: 17th October 2025
#Description: counts number of times a given character appears in a given string

word = input("Enter word: ")
chara = input("Enter character: ")

'''print(chara, 'occurs in', word, word.count(chara), 'times')'''# quicker way

count = 0
for o in word:
    if o == chara:
        count = count+1
    else:
        pass
print(chara, 'occurs in', word, count, 'times')
