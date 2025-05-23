# This program was built to say greetings to the entered name
# It can be 'Good morning/afternoon/evening/night'. Depends on the local time of the computer
# Was created using time module :D

import time
name = input("Enter your name: ")
hour = time.strftime("%H")


def greeting_name(name):
    if hour == "05" or hour == "06" or hour == "07" or hour == "08" or hour == "09" or hour == "10" or hour == "11":
        return f"Good morning {name}!"
    elif hour == "12" or hour == "13" or hour == "14" or hour == "15" or hour == "16" or hour == "17":
        return f"Good afternoon {name}!"
    elif hour == "18" or hour == "19" or hour == "20" or hour == "21" or hour == "22" or hour == "23":
        return f"Good evening {name}!"
    elif hour == "00" or hour == "01" or hour == "02" or hour == "03" or hour == "04":
        return f"Good night {name}!"


print(greeting_name(name))