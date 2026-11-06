#Author: Vira Ustymenko
#Date: 5th November, 2026
#Description: Recursive function to get the sum of the digits of a non-negative integer


def boo(hive):
    if len(str(hive)) == 0:
        return 0
    else:
        return int(boo(str(hive)[1:]))+int(str(hive)[0])

frederick = 901432
x = boo(frederick)
print(x)