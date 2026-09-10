#Author: Vira Ustymenko
#Date: 10th September
#Description: Bubble sort method - Version 3

L1 = [10,8,6,4,2]
iterat = len(L1)-1

for b in range(iterat):
    test = False
    for i in range(iterat-b): #< -- checking one less element each iteration
        if L1[i]>L1[i+1]:
            big = L1[i]
            L1[i]=L1[i+1]
            L1[i+1]=big
            test = True
    if not test:    #checks if there have been swaps
        break
            
print(L1)
            