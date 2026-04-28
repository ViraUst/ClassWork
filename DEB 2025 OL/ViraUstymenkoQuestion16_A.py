#Question 16(a)
#Name and School: Vira Ustymenko
#Date: 28th April 2026

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit-32)*5/9 
    return celsius

def kelvin(celsius):
    kelvin = celsius+ 273.15
    return kelvin

conversion= input("Enter 1 for Celsius to Fahrenheit conversion and 2 for Fahrenheit to Celsius conversion: ")

if conversion == '1': #conditional
    celsius = float(input("Enter the temperature in Celsius: "))
    print(celsius,"C",chr(176),"is equal to",round(celsius_to_fahrenheit(celsius),2),"F",chr(176), "and",round(kelvin(celsius),2),\
          "K")
elif conversion == '2': #conditional
    fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
    celsius = round(fahrenheit_to_celsius(fahrenheit),2)
    print(fahrenheit,"F",chr(176), "is equal to",celsius,"C",chr(176), "and",round(kelvin(celsius),2),\
          "K")
