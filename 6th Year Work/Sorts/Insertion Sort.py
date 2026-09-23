#Author: Vira Ustymneko
#Date: 23rd September, 2026
#Description: Insertion sort

L1 = [11,7,14,19,12]
marker = L1[0]

for i in range(1,len(L1)):
    marker = L1[i]
    for j in range(i-1,-1,-1):
        if L1[j]>marker:
            swap = L1[j]
            L1[j]=L1[j+1]
            L1[j+1]=swap
            print(L1)
        else:
            break
print(L1)