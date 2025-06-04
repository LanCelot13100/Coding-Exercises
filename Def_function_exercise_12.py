# This program is the copy of 'Def_function_exercise_5' but here I used 'try' and 'except' technologies to avoid mistakes
# Was created using 'def' function + 'try' and 'except' technologies :D

while True:
    def check_data_type():
        question1 = input("Enter the weather outside (Q to quit): ")
        def weather(question):
            if int(question) > 30:
                return "It's hot."
            elif int(question) >= 15:
                return "It's a nice day!"
            elif int(question) > 0:
                return "It's a bit cold..."
            else:
                return "It's cold."
        try:
            while question1 :
                int_value = int(question1)
                print(weather(question1))
                question1 = input("Enter the weather outside again (Q to quit): ")
        except ValueError:
                while question1 == "q" or question1:
                    if question1 == "q":
                        print("""The program terminated.
Thanks for using!""")
                        break
                    else:
                        print("You need to enter a number of the temperature outside")
                        break

    check_data_type()

