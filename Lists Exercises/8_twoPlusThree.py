#Author: Vira Ustymenko
#Date: 16th January 2026
#Description: takes any two lists L and M of the same size and adds their elements together to form
#a new list N whose elements are sums of the corresponding elements in L and M.

lit = []
out = []
both = []
demog = False

print("Enter number elements of the list lit, enter demogorgon to finish: ")
while not demog:
    el = input("Element = ")
    if el.isdigit()==True:
        lit.append(el)
    elif el == "demogorgon":
        demog = True
    else:
        print("Please enter a number or the password.")

count = 0
demog = False
print("Enter number elements of the list out: ")
while count!=(len(lit)):
    od = input("Element = ")
    
    if od.isdigit()==True and len(out)<len(lit):
        out.append(od)
    else:
        print("Please enter a number or the password.")
    count +=1


index=0
for i in lit:
    pit = int(i) + int(out[index])
    both.append(pit)
    index +=1
print(both)