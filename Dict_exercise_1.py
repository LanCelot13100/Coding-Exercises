#  In this program I created a technology that separates your name and surname entered in one input using reversed functions and lists
#  Was created using 'dict' + lists :D

name_surname = input("Enter your name and surname: ")
while not " " in name_surname:
    print("You have to enter your name and your surname.")
    name_surname = input("Enter your name and surname again: ")

age = input("Enter you age: ")
name_list = []
surname_list = []


# This function returns your name separated from the other text with the 'space' button
list_name = list(name_surname)
def name_function():
    for row1 in list_name:
        if row1 == " ":
            break
        name_list.append(row1)
    return "".join(name_list)



#  Here we need to reverse our list to get the surname that's been entered after the 'space' button
reversed_list_name = reversed(list_name)
#  This function created the for loop that will help fill the surname_list with the letters of the entered surname
def surname_function():
    for row2 in reversed_list_name:
        if row2 == " ":
            break
        surname_list.append(row2)
    created_surname = list(reversed(surname_list))
    return "".join(created_surname)


name = name_function()
surname = surname_function()

#  These are functions that return the entered name and surname with the uppercase first letter no matter how it was entered

list_name = list(name)
def uppercase_name():
    if list_name[0] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        return "".join(list_name)
    elif list_name[0] in "abcdefghijklmnopqrstuvwxyz":
        list_name[0] = list_name[0].upper()
        new_name_in_function = "".join(list_name)
        return new_name_in_function


list_surname = list(surname)
def uppercase_surname():
    if list_surname[0] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        return "".join(list_surname)
    elif list_surname[0] in "abcdefghijklmnopqrstuvwxyz":
        list_surname[0] = list_surname[0].upper()
        new_name_in_function = "".join(list_surname)
        return new_name_in_function

new_name = uppercase_name()
new_surname = uppercase_surname()

# And this is finally the dictionary...
profile_dict = {}
profile_dict["Name"] = new_name
profile_dict["Surname"] = new_surname
profile_dict["Age"] = age

print(f"""Here is the dictionary that was created using the entered data:"
{profile_dict}""")
