#Author: Vira Ustymenko
#Date: 15th May, 2026
#Description: Ceasar cipher with ord() and chr()

def ceasar_cipher(lock,key,turn):
    end = ord('Z')
    start = ord('A')
    span = end - start + 1
    locked =''
    if turn =='-':
        key = key * -1
    for h in lock:
        if h.isalpha():
            h=h.upper()
            codePointVal = ord(h)
            new_char_num = codePointVal+key
            if new_char_num>end:
                new_char_num = new_char_num-span
            if new_char_num<start:
                new_char_num = new_char_num+span
            locking = chr(new_char_num)
            locked = locked+locking
        else:
            locked = h
    result = locked
    return result

lock = input("Enter a message to en/de crypt: ")
key = int(input("Enter the key for en/de cryption: "))
turn = input("Enter '-' if you wish to DEcrypt, other - press ENTER: ")

x = ceasar_cipher(lock,key,turn)
print(x)
