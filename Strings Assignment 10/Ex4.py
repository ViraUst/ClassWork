#Author: Vira Ustymenko
#Date: 21st October 2025
#Description: removes characters with odd value from a given string
index = 0
word = input("Enter word: ")
newWord = word
while index < len(word):
    if index%2 != 0:
        WordNew = newWord.replace(word[index],'')
        newWord = WordNew
    else:
        pass
    index = index + 1
print(newWord)