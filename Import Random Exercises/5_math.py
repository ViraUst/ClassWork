#Author: Vira Ustymenko
#Date: 9th February, 2026
#Description: makes a math quiz by generating two whole numbers and an operator, each correct answer = +1 to points, runs until
# user enters 'q' to quit.

import random
valueu = 0
points = 0

while valueu != 'q':
    randNum1 = random.randint(1,1000)
    randNum2 = random.randint(1,1000)
    listOp = ['+','-','*','//']
    operator = random.choice(listOp)
    if operator == '+':
        trueAnsw = randNum1 + randNum2
    elif operator == '-':
        trueAnsw = randNum1 - randNum2
    elif operator == '*':
        trueAnsw = randNum1 * randNum2
    elif operator == '//':
        trueAnsw = randNum1 // randNum2
        
    print("Enter 'q' to quit. The equation is: ", randNum1,operator,randNum2)
    valueu = input("Enter the answer: ")
    if valueu == 'q':
        break
    else:
        value = int(valueu)
    if value == trueAnsw:
        points += 1
        print("Correct!    +1 point")
    else:
        print("Incorrect, the correct answer was: ", trueAnsw)
print("Well done! You got: ", points, 'points!')