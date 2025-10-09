#Author: Vira Ustymenko
#Date: 07th October 2025
#Description: program takes N>20 as input, prints numbers in range 11 - N, if N is
# a miltiple of 3 print tipsy, if N is a multiple of 7 prints  topsy, both - prints
#tipsytopsy

N = input("Enter a number > 20: ")
N = int(N)
for i in range(11,N+1):
    print(i)
    if i%3==0 and i%7==0:
        print("TipsyTopsy")
    elif i%3==0:
        print("Tipsy")
    elif i%7==0:
        print("Topsy")
    else:
        pass