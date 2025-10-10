#Author: Vira Ustymenko
#Date: 9th October 2025
#Description: sums seqence (b) - 1**2+3**2+5**2+.....+n**2

n = int(input("Enter integer end of seqence value: "))
theSum = 0
for i in range(n+1):
    if i%2==0:
        pass
    else:
        theSum = i**2 + theSum
print(theSum)