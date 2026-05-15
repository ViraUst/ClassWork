#Author: Vira Ustymenko
#Date: 14th May, 2026
#Description: Ceasar cipher Ex.1

def ceasar_cipher(lock,key,turn):
    Alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    if turn == '-':
        key = key * -1
    else:
        pass
    if key >0 or key<0:
        #encryption -> move to the right
        #decryption <- move to the left
        locked = ''
        lock = lock.upper()
        for i in lock:
            if i.isalpha()==True:
                index = Alpha.index(i)+key
                if index>(len(Alpha)-1):
                    index = index-26
                locking = Alpha[index]
                locked += locking
            else:
                locked+=i
            result = locked
    else:
        result = lock
    return result


lock = input('Enter a message to en/de crypt: ')
key = int(input("Enter key for en/de cryption: "))
turn = input("If you wish to decrypt enter -, else press ENTER: ")
x = ceasar_cipher(lock,key,turn)
print(x)
