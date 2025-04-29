# This program estimates the entered temperature outside
# Was created using 'def' function :D
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
while not question1 == "q":
    print(weather(question1))
    question1 = input("Enter the weather outside again (Q to quit): ")
print("""The program terminated.
Thanks for using!""")

