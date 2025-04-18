# This program asks you for entering the name that's been given to you in the guest list
# If your name is Kyle, the program will be terminated
# If Your name is not Kyle, the program will iterate until you enter the right name
print("""Here is the list of guests:
Jake
Kyle
James
Your name has to be 'Kyle'""")
names = ["jake","kyle","james"]
name0 = names[0]
name1 = names[1]
name2 = names[2]
question = input("Enter your name: ")
while question == name1 or question == name0 or question == name2 or len(question) > 0:
    if question == name1:
        print(f"""Alright!
Jake
Kyle
James
You've entered your name right!""")
        break
    elif question == name0:
        print(f"""Your name is not 'Kyle'
Jake
****
*****
These row has to be extended!""")
        question = input("Enter your name again: ").lower()
    elif question == name2:
        print(f"""Your name is not 'Kyle'
****
****
James
These row has to be completed!""")
        question = input("Enter your name again: ").lower()
    else:
        print("I don't understand that...")
        question = input("Enter your name again: ").lower()





