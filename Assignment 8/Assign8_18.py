#Author: Vira Ustymenko
#Date: 07 October 2025 - 08 October 2025
#Desc: reads int X, determines number of digits, forms an integer Y that
# has the number of digits at ten's place and most significant at one's,
# outputs Y

n = 0
X = input("Enter integer X: ")
for i in X:
    n = n + 1
for b in X:
    break
ten = n*10
b = int(b)
Y = ten + b
print(Y)