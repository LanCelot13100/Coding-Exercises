# That's a basic program that contains not only 'while' loop, but also the 'digit()' method.
# The 'digit()' method checks if characters in the 'question' variable are digits(0-9)

# Here the program checks if the entered value is NOT a digit and the amount fo entered characters is equal to 1
question = input('Enter a letter: ')

while len(question) == 1 and not question.isdigit() or question:
    if not question.isdigit() and len(question) == 1:
        print("""You entered a letter
The program terminated
Thanks for using!""")
        break
        
    else:
        print("You entered smth else!")
        question = input('Enter a letter: ')
