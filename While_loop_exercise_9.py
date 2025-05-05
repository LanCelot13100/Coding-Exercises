# This program asks you to enter 'something' (literally anything) and if you don't enter anything, program will iterate.
# BUT if you enter only the 'space' button, the program will iterate
# Using '.strip()':D
question = input("Enter something: ").strip()
while question == "":
    print("You didn't enter anything!")
    question = input("Enter something again: ").strip()
print("You entered something!")

# This is the second variant of the same technology, but I made it work without '.strip()'
question = input("Enter something: ")
space = " "
while question == "" or question < str(len(space)):
    print("You didn't enter anything!")
    question = input("Enter something again: ")
print("You entered something!")

