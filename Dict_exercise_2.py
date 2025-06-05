#  This program shows you the created dictionary and asks you to enter any key of this dictionary
#  If you enter values of the key, the program will tell you this
#  If you enter something else, the program will tell oy==you this either

profile = {
        "name": "Jack",
        "age": "19",
        "nationality": "American"
}

print("Here is the dictionary that you got:")
for i in profile.items():
    print(i)

question = input("Enter a key: ")


while True:
    if question in profile:
        print(profile.get(question))
        question = input("Enter a key again (Q to quit): ")
    elif question.lower() == "q":
        print("""
The program terminated
Thanks for using!""")
        break
    elif not question in profile:
        if question in list(profile.values()):
            print("You need to enter keys. NOT values to these keys")
            question = input("Enter a key again (Q to quit): ")
        else:
            print("There is not such key in this dictionary")
            question = input("Enter a key again (Q to quit): ")

