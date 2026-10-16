#Author: Vira Ustymenko
#Date: 16th October
#Description: Dictionaries Program 3

failyk = open('book.txt', 'r')
content = failyk.read()
check = dict()
c = []
spill = ''

spilled = content.split()#removes multiple spaces as well as single ' ' spaces

for m in spilled:
    if m not in c:
        check[m]=spilled.count(m)
        c.append(m)
    if m in c:
        pass

def sf(x):
    return x[1]
tuple_sorted_dict = sorted(check.items(),key=sf,reverse=True)
print(tuple_sorted_dict[0:10])