#Author: Vira Ustymenko
#Date: 30th April 2026
#Description: function given a sentence returns it with words reversed

def master_yoda(sentence):
    sentence+=' '
    sent = sentence
    number = sent.count(' ')
    start = 0
    List = []
    for i in range(number):
        occurence = sent.find(' ')
        List.append(sent[:occurence])
        num = start+occurence+1
        sent = sentence[num:]
        start=num
    reverse = List[::-1]
    result = str(reverse)
    for k in result:
        if k in "'[],":
            result=result.replace(k,'')
    
    return result

x = master_yoda('We are ready')
y = master_yoda('I am home')
print(x,'''
''',y)

