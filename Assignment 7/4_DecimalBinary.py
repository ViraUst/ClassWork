#Author: Vira Ustymenko
#Date: 6th October 2025
#Description: converts Decimal to Binary

numThe = int(input("Input Decimal: "))
conv = 0
convert = 1
while numThe>=1:
    conv = numThe%2
    numThe = numThe//2
    print(conv)

