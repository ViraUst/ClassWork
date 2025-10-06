#Author: Vira Ustymenko
#Date: 02 October 2025
#Description: Program takes integers from a user and returns average. Empty string-
#Stop criteria

userNumber = 0
countAvg = 0
couuntNum = 0
while userNumber!='':
    userNumber = input("Please enter an integer, to stop press ENTER: ")
    if userNumber.isdigit()==True:
        userNumber = int(userNumber)
        countAvg = countAvg + 1
        couuntNum = couuntNum + userNumber
        
    ''' line6 - number_ = 0
    line9 - while number_==0:
        userNumber = input("Please enter an integer, to stop press ENTER: ")
        if userNumber == '':
            break
        else:
            userNumber = int(userNumber)
            countAvg = countAvg + 1
            couuntNum = couuntNum + userNumber'''

print('Average of given numbers =', couuntNum/countAvg)