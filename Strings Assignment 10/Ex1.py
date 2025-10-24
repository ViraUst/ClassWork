a = 'apple'
upper = a.upper()
print(upper)

a1 = 'BANANA'
lower = a1.lower()
print(lower)

a2 = 'what'
count = a2.count('w')
print(count)

a3 = 'Pipplepaddleopsocopolis'
find = a3.find('l')
print(find)

a4 = 'Willow'
new = a4.replace('W','P')
print(new)

a5 = 'octopuses'
trueorfalse = a5.islower()
print(trueorfalse)

a6 = 'BUNNY'
treu = a6.isupper()
print(treu)

a7 = '25 kittens!'
cat = a7.isalnum()
print(cat)

a8 = 'Hewwo'
hi = a8.isalpha()
print(hi)

a9 = '277 children were sleeping in 0-0'
w = a9.isdigit()
print(w)

a10 = 'Pipplepaddleopsocopolis'
b = 'paddle'
hm = a10.index('p')
print(hm)

a11 = 'The paddle grew big, but I managed to stay dry walking over it.**'
ffd = a11.strip('*')
print(ffd)