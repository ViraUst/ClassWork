#Auhtor: Vira Ustymenko
#Date: 12th February 2026
#Description: determine all two-digit numbers the sum of squares of which is equal to the sum of squares of them with reversed digits
# (three number combinations)

for a in range(10,100):
    for b in range(10,100):
        for c in range(10,100):
            eq1 = (a**2)+(b**2)+(c**2)
            a1 = str(a)[::-1]
            b1 = str(b)[::-1]
            c1 = str(c)[::-1]
            eq2 = (int(a1))**2+(int(b1))**2+(int(c1))**2
            if eq1 == eq2:
                print(a,'^2 ',b,'^2 ',c,'^2 ')