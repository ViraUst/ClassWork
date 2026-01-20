#Author: Vira Ustymenko
#Date: 19th January 2026
#Description: Reads two lists num and denum which contain the numerators and denominators of same
#fractions at respective indexes. Then displays the smallest fraction along with its index.

num = [1,2,3,4,5]
denum = [5,2,68,9,12]
smallest = 100
for i in range(len(num)):
    check = num[i]/denum[i]
    if check<smallest:
        smallest = check
        index = i
print("Smallest fraction =", num[index],"/",denum[index])