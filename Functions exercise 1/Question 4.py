#Author: Vira Ustymenko
#Date: 30th April 2026
#Description: function capitalises the first and fourth letters of a name. If the name is too short - error number.

def old_macdonald(word):
    if len(word)<4:
        newWord = -1
    else:
        newWord = word[0].upper() + word[1:3] + word[3].upper() + word[4:]
    return newWord

x = old_macdonald('wor')
y = old_macdonald('macdonald')
print(x,y)