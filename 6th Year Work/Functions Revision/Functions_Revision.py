#Author: Vira Ustymenko
#Date: 24th September, 2026
#Description: Functions for mean, median, mode, frequency, range

'''L = []
k = True
while k:
    add = input("enter a number, when done enter D: ")
    if add.upper() == 'D':
        k = False
    else:
        L.append(float(add))
    
print(L)
 '''   
def meann_func(lis):
    thesum = 0
    for i in lis:
        thesum += i
    mean = thesum/len(lis)
    
    return mean



def mediuman_func(mis):
    lenth = len(mis)
    mis.sort()
    oper = lenth//2
    if lenth%2==0:
        median = (mis[oper]+mis[oper-1])/2
    else:
        median = mis[oper]
        
    return median


def model_func(nis):
    check = 0
    mode = None
    freaqs = []
    for i in nis:
        if check < nis.count(i):
            check = nis.count(i)
            mode = i
        if i not in freaqs:
            freaqs.append(i)
    freaqs.pop(freaqs.index(mode))
    for b in freaqs:
        if nis.count(b)==nis.count(mode):
            mode = None
            break
            
    return mode


def frequent_func(ois):
    los = []
    for i in ois:
        num = ois.count(i)
        ge = str(i) + " appears " + str(num) + " time(s)"
        if ge not in los:
            los.append(ge)
    return los
    
    
def ranger_func(pis):
    pis.sort()
    ranger = pis[-1] - pis[0]
    
    return ranger
'''
x = meann_func(L)
y = mediuman_func(L)
z = model_func(L)
a = frequent_func(L)
b = ranger_func(L)
print(x,y,z,a,b)'''