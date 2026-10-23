#Author: Vira Ustymenko
#Date: 22nd October, 2026
#Description: Word count game?


def score(pint): #function for counting the points for each word
    pinty = pint.upper()
    lenth = len(pint)
    score = 0
    for o in ('A','O','U','E','I'):
        score = score+pinty.count(o)
        lenth -= pinty.count(o)
    for f in ('V','W','X','Y','Z'):
        score = score+pinty.count(f)*5
        lenth -=pinty.count(f)
    score += lenth*3
    return score
    

lever = 'Y' #variable for the loop what lets the program play once
totalscore = 0
Highest = 0 #highest score of a word

while lever.upper()=='Y':
    word = input("Enter a word: ")
    if word.isalpha()!=True:
        bee = False #Boolean variable to determine whether the input fits the requirements
    else:
        bee = True
        
    while not bee: #loop for getting a fitting word
        word = input("Error. Enter a word: ")
        if word.isalpha()==True:
            bee = True
        else:
            pass
    x = score(word)
    wordF = word.upper()
    
    if Highest<x: #condition for determining the highest scoring word at the end of the game
        Highest = x
        Answe = f"Highest scoring word was: {wordF}, {x} points"
    totalscore = totalscore+x
    print(f"Word: {wordF}, Score: {x}, Total score: {totalscore}")
    lever = input("Do you wish to contine?[Y/N]: ")

print(Answe)