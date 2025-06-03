# This program is a fixed copy of 'List_exercise_3' which I was able to make shorter and better.
# I finally solved that problem with returning the entered punctuation marks in sentence one by one how you have entered this!
# In the 'List_exercise_3' a lot of functions returned the punctuation marks one by one how it was declared in the code
# Was created using lists and 'def' functions :D

entered_sentence = input("Enter a sentence with punctuation marks: ")
punctuation_marks = [",",".","!","?","'"]
new_list = []

while entered_sentence == "":
    print("Ooops, looks like you didn't enter any punctuation marks...")
    entered_sentence = input("Enter a sentence with punctuation marks again: ")


def marks(sentence: str):
    for row1 in sentence:
        if row1 in punctuation_marks:
            new_list.append(row1)
    return new_list


# Here the 'new_list' variable has to become a string and back to make it not repeat the same punctuation mark inside itself
string = ("".join(marks(entered_sentence)))
unrepeatable_marks = list(dict.fromkeys(string))

print("Here are the entered punctuation marks one by one:")
for row2 in unrepeatable_marks:
    print(row2)
