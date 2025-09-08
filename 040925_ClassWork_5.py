#Author Vira Ustymenko
#Date: 04 September 2025
'''Description: Program asks the user if it's raining, then asks if it's windy,
if answer = yes displays a message, if answer is no displays other message. If they
didn't answer yes to the first question it says "Enjoy your day"'''

user_rain = input('''Is it raining?
- ''')
if user_rain == "Yes" or user_rain == "yes":
    user_wind = input('''Is it windy?
- ''')
    if user_wind == "Yes" or user_wind == "yes":
        print("It is too windy for an umbrella.")
    elif user_wind == "No" or "no":
        print("Take an ubrella.")

else:
    print("Enjoy your day.")
