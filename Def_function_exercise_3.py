# This program asks to enter any two numbers adding them later
# I really wanted to make a calculator using 'def' function, so here it is!
first = int(input("Enter the first number: "))
second = int(input("Enter the second number: "))
action = input("""Enter the action (What to do with these numbers?) 
>Plus+ (addition)
>Minus- (subtraction)
>Multiply* (multiplication)
>Divide/ (division)
>""").lower()
def addition(x,y):
    return x + y
def subtraction(x,y):
    return x - y
def multiplication(x,y):
    return x * y
def division(x,y):
    return x / y
while action == "plus" or action == "plus+" or action == "addition" or action == "+" or action == "minus" or action == "minus-" or action == "subtraction" or action == "-" or action == "multiply" or action == "multiply*" or action == "multiplication" or action == "*" or action == "divide" or action == "divide/" or action == "division" or action == "/" or action:
    if action == "plus" or action == "plus+" or action == "addition" or action == "+":
        print(f"""The result of addition is equal to {addition(first,second)}
The program has been terminated
Thanks for using!""")
        break
    elif action == "minus" or action == "minus-" or action == "subtraction" or action == "-":
        print(f"""The result of subtraction is equal to {subtraction(first, second)}
The program has been terminated
Thanks for using!""")
        break
    elif action == "multiply" or action == "multiply*" or action == "multiplication" or action == "*":
        print(f"""The result of multiplication is equal to {multiplication(first, second)}
The program has been terminated
Thanks for using!""")
        break
    elif action == "divide" or action == "divide/" or action == "division" or action == "/":
        print(f"""The result of division is equal to {division(first, second)}
The program has been terminated
Thanks for using!""")
        break
    else:
        print("The action wasn't entered right")
        action = input("""Enter the action again (What to do with these numbers?)
>""")


