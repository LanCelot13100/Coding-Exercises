# This program asks you to enter a sentence with punctuation marks giving you only entered punctuation marks after that
# Was created using lists :D
question1 = input("""Enter a sentence with punctuation marks (It's necessary BTW):
> """)
punctuation_marks = [",",".","!","?","'"]
new_list = []
def comma():
    if punctuation_marks[0] in question1:
        return new_list.append(",")
def period():
    if punctuation_marks[1] in question1:
        return new_list.append(".")
def exclamation_mark():
    if punctuation_marks[2] in question1:
        return new_list.append("!")
def question_mark():
    if punctuation_marks[3] in question1:
        return new_list.append("?")
def quote():
    if punctuation_marks[4] in question1:
        return new_list.append("'")
# Here is the base sequence of punctuation marks down below:
comma()
period()
exclamation_mark()
question_mark()
quote()
for row in new_list:
    print(row)
