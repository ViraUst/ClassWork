#Author: Vira Ustymenko
#Date: 1st May 2026
#Description: function, given three integers between 1 and 11, if their sum is <= 21 returns their sum.
#If it exceedes 21 and there's an 11 reduce total sum by 10. If sum exceedes 21, even ater adj returns 'BUST'.

def blackjack(a,b,c):
    Sum = int(a)+int(b)+int(c)
    if Sum<=21:
        result = Sum
    elif Sum> 21 and 11 in [a,b,c]:
        Sum -= 10
    if Sum>21:
        result = 'BUST'
    else:
        result = Sum
    return result

x = blackjack(5,6,7)
y = blackjack(9,9,9)
z = blackjack(9,9,11)

print(x,y,z)