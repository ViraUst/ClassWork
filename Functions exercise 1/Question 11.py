#Author: Vira Ustymenko
#Date: 5th May 2026
#Description: takes in a list of integers and returns True if it contains 007 in order

def spy_game(key):
    firstC = False
    secondC = False
    result = False
    result = False
    for l in key:
        if l == 0 and firstC == False:
            firstC = True
        elif firstC == True and l ==0:
            secondC = True
        if secondC == True and l == 7:
            result = True
    return result

x = spy_game([1,2,4,0,0,7,5])
y = spy_game([1,0,2,4,0,5,7])
z = spy_game([1,7,2,0,4,5,0])

print(x,y,z)