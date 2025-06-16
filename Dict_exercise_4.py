#  This program gives you the dict and suggests us to change the values to the keys
#  We can change the value of 'name', 'surname' and 'age' keys
#  Was created using dicts and **kwargs :D


#  This function replaces the entered keys with new ones
def change_values(the_profile: dict, **kwargs):
    for key1,value1 in kwargs.items():
        if the_profile.get(key1) != value1:
            the_profile[key1] = value1
        return the_profile
#  'the_profile' parameter is the 'main_profile' dict
#  **kwargs are the keys in the 'main_profile' dict


#  This the dictionary that's being shown to us
main_profile = {
    "name": "Ray",
    "surname": "Smith",
    "age": 19
}

print(f"Here is the dictionary: {main_profile}")

#  We can agree to make replace some values or not (If not, the program terminates)
question = input("""Do you want make replace some values?
>Yes
>No (Finish)
> """).lower()

while question == "yes" or question == "no" or question:
    if question == "yes":
        #  Here we can choose the name of the key which value we want to replace
        entered_key = input("Enter a key which value you want to change: ").lower()
        new_new_key = f"'{entered_key}'"
        if entered_key in main_profile.keys():

           #  Here we can change the value to the 'name' key
            if entered_key == "name":
                value = input("Enter a new value for this key: ")
                print(change_values(the_profile=main_profile, name=value))
                question = input("""Do you want to replace some values?
> Yes
> No(Finish)
> """).lower()
            #  Here we can change the value to the 'surname' key
            elif entered_key == "surname":
                value = input("Enter a new value for this key: ")
                print(change_values(the_profile=main_profile, surname=value))
                question = input("""Do you want to replace some values?
> Yes
> No(Finish)
> """).lower()
            #  Here we can change the value to the 'age' key
            elif entered_key == "age":
                value = input("Enter a new value for this key: ")
                print(change_values(the_profile=main_profile, age=value))
                question = input("""Do you want to replace some values?
> Yes
> No(Finish)
> """).lower()
        else:
            #  Here is the notification that the entered 'key' is not in the given dictionary
            print("The entered key is not in the 'user_profile' dictionary")

    elif question == "no":
        print("""The program terminated
Thanks for using!""")
        break

    else:
        #  If the answer of the first question is neither 'Yes' or 'No', the question will iterate
        print("I don't understand that...")
        question = input("""Do you want to replace some values?
>Yes
>No (Finish)
> """).lower()




