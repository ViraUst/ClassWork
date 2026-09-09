#Author: Vira Ustymenko
#Date: 4th September
#Description: Bubble sort method

L1 = [10,8,6,4,2]
iterat = len(L1)-1

var = True
start = 0
nexT = start+1
ver = 0
#while var:
for b in range(iterat):
    for i in range(iterat):
    #start = 0
    #nexT = start+1
        #L2=L1.copy()
        #for b in range(4-ver):
        if L1[i]>L1[i+1]:
            big = L1[i]
            L1[i]=L1[i+1]
            L1[i+1]=big
                #L1.pop(start)
                #L1.insert(nexT,big)
                #start += 1
                #nexT+=1
            #else:
                #pass
        #if L2 == L1:
          #  var = False
       # ver+=1
    #break
            
            
print(L1)
            