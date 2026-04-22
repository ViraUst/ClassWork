# Question 16(b) 
# Name and School: Vira Ustymenko, Athlone Community College
# Date: 22nd April 2026

List1 = [4,5,9,8,10,17,99,77]

lenth = len(List1)

medNum = lenth//2
if lenth%2 == 1:
    median = List1[medNum]
else:
    median = (List1[medNum]+List1[medNum+1])/2

print("Median is:", median)