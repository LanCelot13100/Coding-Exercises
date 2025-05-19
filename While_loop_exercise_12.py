# This program shows you the mathematical table of the entered number from 1 to 10
# If you enter a string, the program will tell you that

number = input("Enter a number from 1 to 10: ")
while True:
    while not (number.isdigit() or number == "q"):
        print("You need to enter a number.")
        number = input("Enter a number from 1 to 10 again (Q to quit): ").lower()
    while not (len(number) == 1 or int(number) == 10):
        print("You need to enter only 1 number")
        number = input("Enter a number from 1 to 10 again (Q to quit): ").lower()
    if number.isdigit():
        for multiply in range(1, 11):
            print(f"{int(number)} * {multiply} = {int(number) * multiply}")
        number = input("Enter a number from 1 to 10 again (Q to quit): ").lower()
    elif number == 'q':
        print("""The program terminated
Thanks for using!""")
        break
