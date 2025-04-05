# This program has to input any number from 0 to 10 and output the OK ("The number has been excepted") or not OK ("IT'S NOT WHAT I ASKED YOU ABOUT")
# This program also has to be terminated when the user presses "Q"
# If the user enters the space button, thr program has to say ("You didn't enter anything...")

x = input("Enter a number between 0 - 10 (Q to quit): ")
while x or x == "":
    if str(x) == "q":
        print("""
The program has been terminated.""")
        break
    elif str(x) == "":
        print("You didn't enter anything")
        x = input("Enter a number between 1 - 10 again (Q to quit): ")
    elif int(x) < 0 or int(x) > 10:
        print("IT'S NOT WHAT I ASKED YOU ABOUT!")
        x = input("Enter a number between 1 - 10 again (Q to quit): ")
    else:
        print("The number was excepted!")
        x = input("Enter a number between 1 - 10 again (Q to quit): ")

