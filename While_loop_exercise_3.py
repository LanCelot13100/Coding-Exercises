# This program asks the user about entering 0 or 1 numbers
# That has to be the while loop
# If the entered number is less than 0, the program has to say "The entered number doesn't have to be negative"
# If the entered number is more than 1, the program has to say "The entered number is more than 0 or 1"
# BUT, If the user enters two same numbers in the row, program has to say that the user has already entered this number!
question = int(input("Enter 0 or 1 numbers: "))
while question == 1 or question == 0 or question > 1 or question < 0:
    if question == 0:
        print(f"You've entered {question}")
        question = int(input("Enter the other number: "))
        while question == 0:
            print(f"You've already entered {question}")
            question = int(input("Enter the other number: "))
    elif question > 1:
        print(f"{question} is more than 0 or 1")
        question = int(input("Enter 0 or 1 numbers: "))
    elif question < 0:
        print("The entered number doesn't have to be negative")
        question = int(input("Enter 0 or 1 numbers: "))
    elif question == 1:
        print(f"You've entered {question}")
        question = int(input("Enter the other number: "))
        while question == 1:
            print(f"You've already entered {question}")
            question = int(input("Enter the other number: "))

