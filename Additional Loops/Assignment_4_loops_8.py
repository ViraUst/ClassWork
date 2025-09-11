#Author: Vira Ustymenko
#Date: 09th September 2025
#Description: Prints the factorial of a given non-negative integer number

userNum = int(input('Enter a non-negative integer number: '))
if userNum > 0:
    print(userNum,end='! = ')
    for put in range(1,(userNum+1)):
        if userNum > 1:
            if put == userNum:
                print(userNum)
            else:
                print(put, end='*')

        else:
            print(put)
    #The line 'else:' just above is for when the entered number is 1
elif userNum == 0:
    print('0! = 1')

elif userNum < 0:
    print('Wrong value entered.')