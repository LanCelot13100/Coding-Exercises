
# This program is the improved copy of 'Def_function_exercise_12'
# Was created using 'def' function + 'try' and 'except' technologies :D


def weather(*,question) -> str:
    if int(question) > 30:
        return "It's hot."
    elif int(question) >= 15:
        return "It's a nice day!"
    elif int(question) > 0:
        return "It's a bit cold..."
    else:
        return "It's cold."

def check_data_type(question_in_function):
    try:
        return weather(question=question1)
    except ValueError:
        return "You need to enter a number of the temperature outside"


while True:
    question1 = input("Enter the weather outside (Q to quit): ").lower()
    if question1 == "q":
        break
    else:
        print(check_data_type(question_in_function=question1))

print("""The program terminated
Thanks for using!""")

