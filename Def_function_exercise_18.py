#  This is the enhanced copy of 'Def_function_exercise_3'
#  Was created using 'lambda' functions and exceptions :D


#  This function accepts the 'action' variable and outputs the action with 2 entered numbers with lambda functions
def decision(*, the_action: str):

    #  Addition:
    if the_action == "add":
        addition = lambda x, y: x + y
        return addition(x=first,y=second)

    #  Subtraction:
    elif the_action == "subtract":
        subtraction = lambda x, y: x - y
        return subtraction(x=first,y=second)

    #  Multiplication:
    elif the_action == "multiply":
        multiplication = lambda x, y: x * y
        return multiplication(x=first,y=second)

    #  Division:
    elif the_action == "divide":
        division = lambda x, y: x / y
        return division(x=first, y=second)


while True:
    try:
        first = int(input("Enter the first number: "))
        second = int(input("Enter the second number: "))

        action = input("""Enter the action (What to do with these numbers?) 
>Add (addition)
>Subtract (subtraction)
>Multiply (multiplication)
>Divide (division)
>""").lower()

        if not (action == "add" or action == "subtract" or action == "multiply" or action == "divide"):
            print("I don't understand.")
            action = input("Enter the action again: ")

        #  This line of code is executing if the entered action was the one that was expected
        print(f"The answer: {decision(the_action=action)}")

        #  Here is the choice between executing the loop again of terminating this:
        question = input("Continue? (Q to finish) ").lower()
        if question == "q":
            break

    #  If the user enters something else instead of numbers, that will be the ValueError that will get the user back to the beginning of the loop
    except ValueError:
        print("You need to enter numbers.")


#  This is the part of code that will wait for the user outside the loop if they press 'Q' after the program executes
print("""The program terminated
Thanks for using!""")

