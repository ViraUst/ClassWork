#Author: Vira Ustymenko
#Date: 15th October, 2026
#Description: program 1 with enhancement 2

sent = input("Please enter a sentence: ")
sent = sent.lower()
space = sent.split(' ')

galaxy = ''

for i in sent:
    if i != ' ':
        galaxy = galaxy + i

#print(space)

dic = dict()

fate = True
print('''
Option 1: count the number of appearances of each word in the sentence

Option 2: count the number of appearances of each letter in the sentence
''')

while fate==True:
    option = input("Choose an option: ")
    if option == '1':
        for i in space:
            count = space.count(i)
            dic[i]=count
        fate = False
    elif option == '2':
        for i in galaxy:
            count1 = galaxy.count(i)
            dic[i]=count1
        fate = False
    else:
        print("Try again.")


    
print(dic)