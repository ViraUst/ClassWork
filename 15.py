#Athor: Vira Ustymenko
#Date: 18.09.25
#Description: prints all natural numbers up to given number

n = float(input("Enter number: "))
n = int(n)

for i in range(1,n):
    if i == n-1:
        print(i)
    else:
        print(i, end=',')
#To make it look cleaner I made it print num.s in one line