#Please enter name: Vira Ustymenko
#Date: 23rd april 2026
#Description: Question 16 B

from datetime import datetime

prompt = input("Please enter prompt:")

if prompt.__contains__("hello") or prompt.__contains__("Hello"):
    print("Hi there, how are you?")
elif prompt.__contains__("name") or prompt.__contains__("Name"):
    print("My name is ExamBot, how can I help?")
elif prompt.__contains__("time") or prompt.__contains__("Time"):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time)
elif prompt.__contains__("weather") or prompt.__contains__("Weather"):
    print("It is always sunny in Ireland.")
else:
    print("I haven't been programmed with an answer to that.")