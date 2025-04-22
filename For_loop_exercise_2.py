# This program needs you to enter any 3 words in the row;
# After that this program will show all these three words in the row and calculate:
# The amount of symbols in each word;
# the amount of symbols in all words.
# BTW, this program won't accept empty lines or space symbols as the 'word' and will iterate over and over again until you enter a real word
space_symbol = " "
first = input("Enter the first word: ")
while len(first) == 0 or first < str(len(space_symbol)):
    print("You didn't enter anything!")
    first = input("Enter the first word again: ")
second = input("Enter the second word: ")
while len(second) == 0 or first < str(len(space_symbol)):
    print("You didn't enter anything!")
    second = input("Enter the second word again: ")
third = input("Enter the third word: ")
while len(third) == 0 or first < str(len(space_symbol)):
    print("You didn't enter anything!")
    third = input("Enter the third word: ")
list_of_words = [first,second,third]
for row in list_of_words:
    print(f"{row}: The amount of symbols in this word is '{len(row)}'")
amount_of_all_symbols = len(first) + len(second) + len(third)
print(f"""
The amount of symbols in all words is '{amount_of_all_symbols}'""")

