# This program asks you to enter the article of the LEGO set
# Let's choose the 7779 article, these four numbers are what you have to enter
# If the entered article is not 7779, then the program prints "It's not the right article"
# If the amount of entered numbers is more than the right amount of numbers (4), the program notifies you about it
# If the user enters the article right, the program terminates
article = input("Enter the article of the set: ")
while not article == "7779":
    if len(article) < 4:
        print("""It's not the right article
There are not enough symbols in this article
The article contains 4 symbols""")
        article = input("Enter the article of the set again: ")
    elif len(article) > 4:
        print("""It's not the right article
There are too many symbols in this article
The article contains 4 symbols""")
        article = input("Enter the article of the set again: ")
    else:
        print("It's not the right article")
        article = input("Enter the article of the set again: ")
print(f"The article {article} has been entered right!")
