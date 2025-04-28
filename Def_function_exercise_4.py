# In this program you need to guess the number (it's 7 actually) and if you don't succeed 3 times, the program will ban you and terminate.
# This program is almost identical to 'While_loop_exercise_4.py' in this repository, but here I used the 'def' function to make it work :D
number = int(input("Guess the number from 1 to 10: "))
one_try = 1
tries = 0
def right_number():
    return 7
while number == right_number() or number != right_number or number < 1 or number > 10:
    if number == right_number():
        print(f"""Yes, you guessed the number right!
It was {right_number()}:D
The program has to be terminated
Thanks for using!""")
        break
    elif number < 1:
        tries += one_try
        print("The entered number doesn't have to be less than 1")
        if tries == 3:
            print("""You've been out of tries,
The system banned you!
Return and try again in some time.
The program has to be terminated
Thanks for using!""")
            break
        number = int(input("Guess the number from 1 to 10 again: "))
    elif number > 10:
        tries += one_try
        print("The entered number doesn't have to be more than 10")
        if tries == 3:
            print("""You've been out of tries,
The system banned you!
Return and try again in some time.
The program has to be terminated
Thanks for using!""")
            break
        number = int(input("Guess the number from 1 to 10 again: "))
    elif number != right_number():
        tries += one_try
        print("You didn't guess that right!")
        if tries == 2:
            print("""You've been out of tries,
The system banned you!
Return and try again in some time.
The program has to be terminated
Thanks for using!""")
            break
        number = int(input("Guess the number from 1 to 10 again: "))
