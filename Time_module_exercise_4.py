# This program asks you to enter the current year, month and day of the current month
# The specific information is down below
# Was created using 'def' function and 'while' loop within that + the 'time' module :D

import time
current_year = time.strftime("%Y")
current_month = time.strftime("%B")
current_day = time.strftime("%d")


def year():
    while True:
        entered_year = input("Enter the current year: ")
        # If the 'entered year' variable is equal to the current year, it will return the entered_year variable for future using
        if entered_year == current_year.lower():
            return entered_year
        # If the 'entered_year' variable doesn't contain digits, the program will say 'I don't understand that'
        elif entered_year and not entered_year.isdigit():
            print("I don't understand that.")
        # If the 'entered_year' variable contains digits, but they are not equal to the current year, the program will tell you that
        elif entered_year and entered_year.isdigit():
            print(f"The current year is not {entered_year}.")


def month():
    while True:
        entered_month = input("Enter the current month: ").lower()
        # If the 'entered_month' variable is equal to the current month, it will return the entered_month variable for future using
        if entered_month == current_month.lower():
            return entered_month
        # If the 'entered_month' variable contains digits, it will tell you to enter the current month with words
        elif entered_month and entered_month.isdigit():
            print("You have to enter the current month with words.")
        # If the 'entered_month' doesn't contain digits, but the entered value is still not equal to the current month,the program will tell you about that
        elif entered_month and not entered_month.isdigit():
            print(f"The current month is not {entered_month}.")


def day():
    while True:
        entered_day = input("Enter the current day: ")
        # If the 'entered_day' variable is equal to the current day, it will return the entered_day variable for future using
        if entered_day == current_day.lower():
            return entered_day
        # If entered_day doesn't contain digits, the program will tell you to enter the day of the current month with numbers
        elif entered_day and not entered_day.isdigit():
            print(f"You have to enter the current day of {current_month} with numbers.")
        # If the 'entered_day' doesn't contain digits, but the entered value is still not equal to the current day of the current month,the program will tell you about that
        elif entered_day and entered_day.isdigit():
            print(f"The current month is not {entered_day}.")


year()
month()
day()
print(f"""That's right!
Today is {current_month} {current_day} of {current_year}!

The program terminated
Thanks for using!""")

