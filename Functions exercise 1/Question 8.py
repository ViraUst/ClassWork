#Author: Vira Ustymenko
#Date: 1st May 2026
#Description: function, given a string, returns a string where for every character in the original there are
# three characters

def paper_doll(char):
    newString = ''
    for i in range(len(char)):
        newString += char[i]*3
    end = newString
    return end

x = paper_doll('Hello')
y = paper_doll('Mississippi')

print(x,y)