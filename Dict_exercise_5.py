#  This program allow you to create 3 own dictionaries that will contain the entered name and age
#  Later, the program extracts the youngest person in all profiles based on the 'age' key of every dict


#  This function separates the name and age entered on the same string returning the tuple of entered name and age
def separating_name_age(*,input_function: list) -> tuple:
    #  This thing is for the name down below:
    name = []
    for row1 in input_function:
        name.append(row1)
        if row1 == ",":
            break
    name.remove(",")

    #  And this thing is for the age:
    age = []
    input_function.reverse()
    for row2 in input_function:
         age.append(row2)
         if row2 == ",":
             break
    age.remove(",")
    age.reverse()
    return name,age


people = []
dict_amount = False
while not len(people) == 3:

    #  If this is the first created profile (without 'again')
    if dict_amount == False:
        input1 = list(input("Enter the name and age of the first person separated by comma: "))
    #  If this is NOT the first created profile (with 'again')
    else:
        input1 = list(input("Enter the name and age of the first person separated by comma again: "))


    #  If the entered data doesn't contain the separating comma, it will tell us about it
    while not "," in input1:
        print("You have to put a comma between the name and age of the first person.")
        input1 = list(input("Enter the name and age of the first person separated by comma: "))

    #  Here we need to unpack the returned value from the 'input_function' function
    real_name, real_age = separating_name_age(input_function=input1)
    #  Now we need to turn the unpacked list of the name into a string
    dict_name = "".join(real_name)
    #  Now we have to capitalize the name to make it look more beautiful ;)
    new_dict_name = str(dict_name.capitalize())
    #  Now we need to turn the unpacked list of the age into a string
    dict_age = "".join(real_age)
    #  Here we just turn the age string into an integer because it has to an int
    new_dict_age = int(dict_age)

    #  Now we create a new list of dictionaries called 'people' and print it
    people.append({"name": new_dict_name, "age": new_dict_age})
    print(f"""
Here are all created profiles: {people}
""")
    dict_amount = True

#  This labda function extracts the youngest person in all profiles based on the 'age' key of every dict
youngest = min(people,key = lambda person: person["age"])
print(f"""Here is the profile of the youngest person:{youngest}

The program terminated
Thanks for using!""")
