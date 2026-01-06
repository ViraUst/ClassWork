#Author: Vira Ustymenko
#Date: 5th January 2026
#Description: Question A, Nov. Assessment, method 1

cardNo = input('''Welcome to CardCheck. Enter your card number: ''')
#7200828282828210 - input options
#8549018035096133 --^

continueWithCheck = False #boolean use
tri = 0

while len(cardNo) != 16: #boolean
    if tri < 2: #boolean
        continueWithCheck = True #boolean
    else:
        continueWithCheck = False #boolean
        break
    cardNo = input("That is incorrect, please try again: ")
    tri = tri+1
    
if len(cardNo) == 16: #boolean
    continueWithCheck = True #boolean
cardN = int(cardNo)

if not continueWithCheck: #boolean
    print("You are blocked due to invalid input")
    
else:
    expire = int(input("Enter the card expiry date e.g. 11/26 should be entered as 1126: "))
    #0425 - input options
    #0324 --^
    
    while cardN>10: #boolean
        cardN = cardN//10
    if cardN == 7: #boolean
        print("This is a ZincCard")
    elif cardN == 8: #boolean
        print("This is a WinCard")
    cvv = 0
    while expire >0: #boolean
        cvv = expire%10 + cvv
        expire = expire//10
    cvv = cvv*int(cardNo[0:2])
    cvv = cvv-int(cardNo[9])
    print("CVV number: ", cvv)
    
    newNum = ''
    EndNum = ''
    start = 0
    end = 4
    for i in range(3): #boolean
        newNum = cardNo[start:end]+'-'
        EndNum = EndNum + newNum
        start = start + 4
        end = end + 4
    print("Card Number: ", EndNum+cardNo[start:end], "and it is valid")
