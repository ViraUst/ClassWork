#Author: Vira Ustymenko
#Date: 25th November 2025
#Description: Program converts Hexadecimal number to Unicode

meh = input('Enter U+: ')
setBinary = ''
finalNum = ''

for tot in meh:
    if tot.isdigit() == True:
        osnova = int(tot)
        while osnova>=1:
            reshtka = osnova%2
            osnova = osnova//2
            setBinary = str(reshtka) + setBinary
        BinaryWithzero = '0'*(4-len(setBinary)) + setBinary
    else:
        if tot == 'A':
            tot = 10
        elif tot == 'B':
            tot = 11
        elif tot == 'C':
            tot = 12
        elif tot == 'D':
            tot = 13
        elif tot == 'E':
            tot = 14
        elif tot == 'F':
            tot = 15
        osnova = int(tot)
        while osnova>=1:
            reshtka = osnova%2
            osnova = osnova//2
            setBinary = str(reshtka) + setBinary
        BinaryWithzero = '0'*(4-len(setBinary)) + setBinary
    finalNum = finalNum + BinaryWithzero
    setBinary = ''

lenth = len(finalNum)
if lenth<=7:
    pi = '0' + '0'*(7-lenth) + finalNum
elif lenth<=11:
    fur = '10'+finalNum[-6:]
    pi = '110'+('0'*(11-lenth))+finalNum[:-6] + fur
elif lenth<=16:
    fur = '10'+finalNum[-12:-6]+'10'+finalNum[-6:]
    pi = '1110'+('0'*(16-lenth))+finalNum[:-12] + fur
elif lenth<=21:
    fur = '10'+ finalNum[-18:-12] +'10'+finalNum[-12:-6]+'10'+finalNum[-6:]
    pi = '11110'+('0'*(16-lenth))+finalNum[:-18] + fur
    
print("UTF-8 =",pi)
    