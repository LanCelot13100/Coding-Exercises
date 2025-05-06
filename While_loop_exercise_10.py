# This program was based on 'Def_function_exercise_5' but here I used 'isdigit()' method + 'lstrip()' methods:
# The 'isdigit()' method checks if all characters in 'question1' variable are digits
# The 'lstrip()' method makes negative numbers a part of range of digits
# Was created using 'while' loop + 'def' function + 'isdigit()' with 'lstrip()' methods :D
question1 = input("Enter the weather outside (Q to quit): ").lower()
def weather(question):
    if int(question) > 30:
        return "It's hot."
    elif int(question) >= 15:
        return "It's a nice day!"
    elif int(question) > 0:
        return "It's a bit cold..."
    else:
        return "It's cold."
while question1 == "q" or question1.lstrip("-").isdigit() or len(question1) > 0:
    if question1.lstrip("-").isdigit():
        question1 = int(question1)
        print(weather(question1))
        question1 = input("Enter the weather outside again (Q to quit): ").lower()
    elif question1 == "q":
        print("""The program terminated.
Thanks for using!""")
        break
    else:
        print("You need to enter the number of the temperature outside")
        question1 = input("Enter the weather outside again (Q to quit): ").lower()

