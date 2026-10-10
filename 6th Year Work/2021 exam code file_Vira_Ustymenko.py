# Question 16(a)
# Examination Number:

# function definition used in part (v)
def is_anagram(w1, w2):
    if sorted(w1.upper()) == sorted(w2.upper()):
        return True
    else:
        return False

word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")
# test whether the sorted strings are the same as each other
# if the sorted strings are the same then they must be anagrams
if (sorted(word1.upper()) == sorted(word2.upper())):
    print(word1,"is an anagram of", word2)
else:
    print(word1, "is NOT an anagram of", word2)
    
x = is_anagram(word1,word2)
if x:
    print(word1,"is an anagram of", word2)
elif not x:
    print(word1, "is NOT an anagram of", word2)
    
phrase1 = input("Enter a phrase: ")
phrase = ''
for i in phrase1:
    if i != ' ':
        phrase = phrase+i.upper()
    
if (sorted(word1.upper()) == sorted(phrase.upper())):
    print(word1,"is an anagram of", phrase)
else:
    print(word1,"is NOT an anagram of", phrase)
    
if (sorted(word2.upper()) == sorted(phrase.upper())):
    print(word2,"is an anagram of", phrase1)
else:
    print(word2,"is NOT an anagram of", phrase1)