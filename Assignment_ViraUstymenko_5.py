#Author: Vira Ustymenko
#Date: 01 September 2025
#Description: Program requests the starting num. of pizza slices and the eaten num. of them, then displays what is left over.
startPizza = int(input("Enter the number of pizza slices you started with: "))
eatenPizza = int(input("Enter the number of pizza slices you have eaten: "))
leftOver = startPizza - eatenPizza
print("There is", leftOver, "pizza slices left over.")
