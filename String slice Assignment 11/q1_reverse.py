#Author: Vira Ustymenko
#Date: 23st October 2025
#Description: reverses string woth a for loop, a while loop, and slicing
string = ''
word = input('enter word: ')
index = 0
for i in word:
    string = i + string
   # index = index-1
   # print(word[index], )
print(string)
#for loop


index1 = 0
index2 = 0
p=0
stringA = ''
while p != len(word):
    stringA = word[index2] + stringA
    index2 = index2 + 1
   # index1 = index1 - 1
   # print(word[index1])
    p = p+1
print(stringA)


#while loop
print(word[::-1])
#slicing