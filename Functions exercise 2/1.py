#Author: Vira Ustymenko
#Date: 5th May 2026
#Description: exercise 2

#1
def range_of_number(kay):
    giant = -999
    tiny = 99999999
    for i in kay:
        if i>giant:
            giant = i
    for i in kay:
        if i<tiny:
            tiny = i
    result = giant - tiny
    return result

#2
def average_of_number(koy):
    ssuma = 0
    numOFnum = 0
    for b in koy:
        ssuma+=b
        numOFnum += 1
    average = ssuma/numOFnum
    return average

#3
def median_number(kiy):
    kiy.sort()
    lenth = len(kiy)
    if lenth%2==0:
        median = (kiy[lenth//2]+kiy[lenth//2-1])/2
    else:
        median = kiy[lenth//2]
        
    return median

#4
def mode_num(kyy):
    for o in range(len(kyy)):
        num = kyy.count(o)
        if num >1:
            mode = o
            break
        else:
            mode = None
    return mode

#5
def input_frequency(kuy):
    ind = 0
    words = "The number "
    l = []
    for i in kuy:
        number = kuy.count(i)
        new = words+str(int(i))+" occurs",str(number),"times."
        l.append(new)
    other = str(l)
    other = other.replace("[",'')
    other = other.replace("]",'')
    other = other.replace(",",'')
    other = other.replace("'",'')
    other = other.replace("(",'')
    other = other.replace(")",'')
    return other

new = 0
key = []
while new != 'Gnome':
    new = input("Enter a list of numbers. When done enter 'Gnome': ")
    if new=='Gnome':
        break
    naw = float(new)
    key.append(naw)
print(key)
z = range_of_number(key)
y = average_of_number(key)
x = median_number(key)
w = mode_num(key)
v = input_frequency(key)

print(z,y,x,w,v)