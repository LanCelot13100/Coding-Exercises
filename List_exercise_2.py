# This program asks you to enter three fruits, but the program will ask you to enter a fruit again if you enter something wrong.
# Was created using lists :D
input("""Here is the list of fruits:
Apple
Banana
Cherry
You need to enter them all in the row! (Press any button to continue)
""")
fruit1 = input("Enter the first fruit: ").lower()
fruit2 = input("Enter the second fruit: ").lower()
fruit3 = input("Enter the third fruit: ").lower()
fruit_list = ["apple","banana","cherry"]
while fruit1 != fruit_list[0] or fruit2 != fruit_list[1] or fruit3 != fruit_list[2] or fruit1 == fruit_list[0] or fruit2 == fruit_list[1] or fruit3 == fruit_list[2]:
    if fruit1 != fruit_list[0]:
        print("The first fruit wasn't entered right.")
        fruit1 = input("Enter the first fruit again: ").lower()
    elif fruit2 != fruit_list[1]:
        print("The second fruit wasn't entered right.")
        fruit2 = input("Enter the second fruit again: ").lower()
    elif fruit3 != fruit_list[2]:
        print("The third fruit wasn't entered right.")
        fruit3 = input("Enter the third fruit again: ").lower()
    else:
        print("""All fruits were entered right!
The program terminated
Thanks for using!""")
        break
