# Question 16(b)
# Name and School: Vira Ustymenko, Athlone Community College
# Date: 16th April 2026

flight_number= input("Enter your flight number: ")
#122,125,132,135,155
direct = 0
indirect = 0
if flight_number[-1] == '2':
    flight_type = 'direct'
    direct += 1
elif flight_number[-1] == '5':
    flight_type = 'indirect'
    indirect += 1
print("Type: ", flight_type)