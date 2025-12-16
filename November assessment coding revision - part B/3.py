#Author: Vira Ustymenko
#Date: 15th December 2025
#Description: Q.16, (b) program from Nov. assessment. 3rd method

cardNumber = '8549018035096133'
lastOne = cardNumber[-1:]
CardMinus1 = cardNumber[:-1]
#Step 1 done

Reverse = ''
for i in CardMinus1:
    Reverse = i + Reverse
#Step 2 done

SumOdd = 0
SumEven = 0
indice = 0
for ok in range(len(Reverse)):
    ok = Reverse[indice]
    if indice%2 == 0:
        doble = int(ok)*2
        if doble>9:
            doble = doble-9
        SumEven = SumEven + doble
    else:
        SumOdd = SumOdd + int(ok)
    indice = indice+1
#Step 3 done

total = SumOdd + SumEven + int(lastOne)
#Step 4 done

if total%10 == 0:
    print("card valid")
else:
    print("card invalid")
#Step 5 done