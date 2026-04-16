# Question 16 (a)
# Name and School: Vira Ustymenko, Athlone Community College
# Date: 16th April 2026

flight_num=input("Enter your flight number: ")
#EI121
#EI125
destination= input("Enter your destination: ")
#Orlando
num_ppl= int(input("Enter the number of people in the travel group: "))
#7
num_kinder = int(input("Enter the number of children in the travel group: "))
print('''Your flight number is''', flight_num, '''
You are travelling to''', destination, '''
There are''', num_ppl,'''people in the travel group''')

if flight_num == "EI121" or flight_num == "ei121":
    Cost = 520
elif flight_num == "EI125" or flight_num == "ei125":
    Cost = 400
totalCost = Cost*num_ppl - num_kinder*50
print('''The total cost of your flight is \u20ac''',totalCost,sep='')