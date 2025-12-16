#Author: Vira Ustymenko
#Date: 15th December 2025
#Description: Q.16, (b) program from Nov. assessment. 2nd method

cardNumber = '8549018035096133'
lastOne = cardNumber[-1:]
CardMinus1 = cardNumber[:-1]
#Step 1 done

Reversed = ''
for i in CardMinus1:
    Reversed = i + Reversed
#Step 2 done

even = ''
indice1 = 0
indice2 = 1
odd = ''
for o in range((len(Reversed)//2)+1):
    even = even + Reversed[indice1]
    indice1 = indice1 + 2
    
for k in range((len(Reversed)//2)):
    odd = odd + Reversed[indice2]
    indice2 = indice2 + 2

SumEven = 0
for e in even:
    doble = int(e)*2
    if doble>9:
        doble = doble-9
    SumEven = SumEven + doble

SumOdd = 0
for d in odd:
    SumOdd = int(d) + SumOdd
#Step 3 done

total = SumOdd + SumEven + int(lastOne)
#Step 4 done

if total%10 == 0:
    print("card valid")
else:
    print("card invalid")
#Step 5 done