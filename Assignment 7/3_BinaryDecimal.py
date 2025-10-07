#Author: Vira Ustymenko
#Date: 6th October 2025
#Description: converts Binary to Decimal
count = 0
theNum = input("Input Binary: ")
power = len(theNum)-1
for i in theNum:
    f = float(i) * (2**power)
    power = power -1
    count = f + count
print("Decimal = ",count)