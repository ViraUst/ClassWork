#Author: Vira Ustymenko
#Date: 17th October 2025
#Description: asks user for a word, if starts with a vowel - 'way' at the end, if
# starts with consonant - first letter to the end and add 'ay' at the end

word = input("Enter a word: ")
if word[0] in 'aeiou':
#word[0]=='a' or word[0]=='o' or word[0]=='i' or word[0]=='u' or word[0]=='e':
    wordmod = word + 'way'
    print(wordmod)
else:
    wordmod1 = (word.replace(word[0],'')) + word[0] + 'ay'
    print(wordmod1)

'''NewWord = ''

if word[0] in 'aoeiu':
    wordnew = word + 'way'
    print(wordnew)
    
else:
    for i in range(1,len(word)):
        NewWord = NewWord + word[i]
    
    finMod = NewWord+word[0]+'ay'
    print(finMod)'''
#alt. way above
