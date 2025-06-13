#  This program creates a dictionary and needs you to enter a key and the value to this key collecting and printing that all
#  Was created using 'def' functions and **kwargs :D
dictionary = {}


#  This function turns the created dictionary into a tuple and prints the key and value in the 'for' loop
def display_data(**data):
    for key,value in data.items():
        print(f"{key} - {value}")
#  The **data is the created dictionary


new_key = input("Enter a new key: ")
new_value = input("Enter the value to this key: ")
dictionary[new_key] = new_value

while new_key and new_value:
    display_data(**dictionary)

    new_key = input("Enter a new key (Q to quit): ")
    #  If you enter 'Q' or 'q', the program will terminate
    if new_key == "Q" or new_key == "q":
        print("""
The program terminated
Thanks for using!""")
        break
    new_value = input("Enter the value to this key (Q to quit): ")
    #  If you enter 'Q' or 'q', the program will terminate
    if new_value == "Q" or new_key == "q":
        print("""
The program terminated
Thanks for using!""")
        break

    dictionary.update([(new_key,new_value)])

