#Author: Vira Ustymenko
#Date: 25th September, 2026
#Description: checking import of functions

from Functions_Revision import meann_func, mediuman_func, model_func, frequent_func, ranger_func

L = [1,2,2,2,45]

'''L = []
k = True
while k:
    add = input("enter a number, when done enter D: ")
    if add.upper() == 'D':
        k = False
    else:
        L.append(float(add))
    
print("Your list = ",L)'''


x = meann_func(L)
y = mediuman_func(L)
z = model_func(L)
a = frequent_func(L)
b = ranger_func(L)


print('''mean = ''', x,'''
median = ''',y, '''
mode = ''',z,'''
frequencies = ''',a,'''
range = ''',b)