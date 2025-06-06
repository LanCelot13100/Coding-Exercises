#  This is the technology that converts any type of values into a string in a dictionary
#  That will be able to help work with this value later in the future projects :D

profile = {
        "name": "Jack",
        "age": 19,
        "nationality": "American",
        "city": "Los Angeles"
}


#  This function accepts the integer in the 'age' key and returns that as a string
def age_change():
    new_age = str(profile.get("age"))
    return new_age


str_age = age_change()

profile.update(age=str_age)
print(profile)
