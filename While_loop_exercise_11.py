# These are three examples of the program that does the same thing down below:

# This one prints every letter in the entered word in the row
# Was created using 'for' loop :D
word = input("Enter any word: ")
for row in word:
    print(row)

# This does the same thing
# Was created using 'while' loop :D
word = input("Enter any word: ")
amount_of_characters = 0
while amount_of_characters < len(word):
    print(word[amount_of_characters])
    amount_of_characters += 1

# This does the same thing too, it was created using 'list()' function and 'while' loop respectively :D
word = input("Enter any word: ")
my_list = list(word)
amount_of_characters = 0
while amount_of_characters < len(my_list):
    print(word[amount_of_characters])
    amount_of_characters += 1

