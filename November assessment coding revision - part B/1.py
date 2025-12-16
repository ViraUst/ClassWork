#Author: Vira Ustymenko
#Date: 15th December 2025
#Description: Q.16, (b) program from Nov. assessment. 1st method

cardNumber = '8549018035096133'
lastOne = cardNumber[-1:]
CardMinus1 = cardNumber[-2::-1]
#Step 1 and 2 done


even = CardMinus1[::2]
odd = CardMinus1[1::2]

evenSum = 0
oddSum = 0

for i in even:
    doble = int(i)*2
    if doble>9:
        doble = doble - 9
    evenSum = evenSum+doble

for o in odd:
    dbl = int(o)
    oddSum = oddSum+dbl
#Step 3 done

total = oddSum + evenSum + int(lastOne)
#Step 4 done

if total%10 == 0:
    print("card valid")
else:
    print("card invalid")
#Step 5 done