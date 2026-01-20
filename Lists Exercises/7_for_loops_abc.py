#Author: Vira Ustymenko
#Date: 16th January 2026
#Description: create following lists using a for loop: a) list consisting of the integers 0 - 49
#b) list containing the squares of the integers 1 - 50
#c) list ['a','bb','ccc','dddd',...] that ends with 26 copies of the letter z.

#a)
l = []
for m in range(50):
    l.append(m)
print("List a: ")
print(l)

#b)
n = []
for o in range(1,51):
    p = o**2
    n.append(p)
print("List b: ")
print(n)

#c)
q = []
teat = 'abcdefghijklmnopqrstuvwxyz'
var = 1
for r in teat:
    s = r*var
    q.append(s)
    var+=1
print("List c: ")
print(q)