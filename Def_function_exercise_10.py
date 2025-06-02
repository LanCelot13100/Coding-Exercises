# This program was actually based on 'While_loop_exercise_6', but here it was rewritten using 'def' functions and the 'isdigit' method

article = input("Enter the article of the set: ")

#Here is the function that determines the amount of numbers in the entered article
def len_article(amount: str):
    right_article = "7779"

    if len(amount) == 4 and article == right_article:
        return f"""The article {article} has been entered right!
        
The program terminated
Thanks for using!"""
    elif  len(amount) == 4 and article != right_article:
        return f"It's not the right article"
    elif len(amount) < 4:
        return f"""It's not the right article
There are not enough symbols in this article
The article contains 4 symbols"""
    elif len(amount) > 4:
        return """It's not the right article
There are too many symbols in this article
The article contains 4 symbols"""


while True:
    # If the entered article is equal to the right one, then the program tells you that and terminates
    if article == "7779":
        print(len_article(amount = article))
        break

    # If the entered article doesn't contain digits, the program will tell you that the right article must contain them
    elif not article.isdigit():
        print("You have to enter the numbers of the article")
        article = input("Enter the article of the set again: ")
    # If the entered article contains digits and it's not equal to the right article, the 'len_article' function is being used
    else:
        print(len_article(amount = article))
        article = input("Enter the article of the set again: ")
