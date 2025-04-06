# This program has to ask the user about their ages work experience
# If it's less that at least 1, the program has to say that it's not enough
# else: OK (You've been hired!)

question = int(input("How many ages of work experience do you have? "))
while question == 0 or question > 0:
    if question == 0:
        print("It's not enough")
        print("We'll call right back")
        question = int(input("How many ages of work experience do you have? "))
    else:
        print("Alright, I think You are exact that one who we've needed!")
        break


