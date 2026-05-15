#Author: Vira Ustymenko
#Date: 15th May 2026
#Description: Question 5 with feedback changes

def master_yoda(sentence):
    sent = sentence.split(' ')
    start = 0
    result = str(sent[::-1])
    for k in result:
        if k in "'[],":
            result=result.replace(k,'')
    return result

x = master_yoda('We are ready')
y = master_yoda('I am home')
print(x,'''
''',y)
