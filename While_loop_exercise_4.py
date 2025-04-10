print("""You need to enter your age down below
It has to be more than 17 years old
You have only 3 tries to enter this
If you don't succeed, the program will ban you""")
question = int(input("Enter your age: "))
try_ = 0
while question > 17 and try_ < 2 or question > 17 and try_ == 2 or question <= 17 or question <= 17 and try_ == 2:
    if question > 17 and try_ < 2:
        print("Welcome!")
        break
    elif question > 17 and try_ == 2:
        print("Welcome!")
        break
    elif question <= 17 and try_ == 2:
        print("")
        print("You've wasted all your tries")
        print("The program has banned you")
        print("try it out again later...")
        break
    else:
        try_ += 1
        print("Your age is not appropriate for this")
        question = int(input("Enter any number again: "))
