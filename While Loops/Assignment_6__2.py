#Author: Vira Ustymenko
#Date: 02 October 2025
#Description: Program takes grades from user and returns average and letter grade of
# the average.

testGrades = 0
countAvg = 0
testGrade = 0
while testGrade>=0:
    testGrade = float(input("Enter your grade: "))
    if testGrade>=0:
        countAvg = countAvg + 1
        testGrades = testGrade + testGrades
    else:
        break

Average = testGrades/countAvg
if Average <= 59:
    print("Average grade: ", Average, ',', 'F')
elif Average > 59 and Average <= 69:
    print("Average grade: ", Average, ',', 'D')
elif Average > 69 and Average <= 79:
    print("Average grade: ", Average, ',', 'C')
elif Average > 79 and Average <= 89:
    print("Average grade: ", Average, ',', 'B')
else:
    print("Average grade: ", Average, ',', 'A')