# This program asks you to enter the fruits that will be put on your plate if you enter 'Quit'
# If you enter a fruit more than 1 time, the program will notice that and tell you about it.
# Was created using lists :D
plate = []
same_apple = 0
same_grapes = 0
same_orange = 0
same_cherry = 0
same_kiwi = 0
print("""Here is the list of fruits that you can put on your plate down below:
Apple
Grapes
Orange
Cherry
Kiwi""")
fruit = input("Enter a fruit: ").lower()
while fruit == 'apple' or fruit == "grapes" or fruit == 'orange' or fruit == 'cherry' or fruit == 'kiwi' or fruit == 'quit' or len(fruit) > 0:
    if fruit == 'apple':
        if same_apple > 0:
            print(f"You've already put {fruit} on your plate.")
            fruit = input("Enter another fruit (>Quit to see your plate): ").lower()
        else:
            same_apple += 1
            plate.append("Apple")
            fruit = input("Enter another fruit (>Quit to see your plate): ").lower()
    elif fruit == 'grapes':
        if same_grapes > 0:
            print(f"You've already put {fruit} on your plate.")
            fruit = input("Enter another fruit (>Quit to see your plate): ").lower()
        else:
            same_grapes += 1
            plate.append("Grapes")
            fruit = input("Enter another fruit (>Quit to see your plate): ").lower()
    elif fruit == 'orange':
        if same_orange > 0:
            print(f"You've already put {fruit} on your plate.")
            fruit = input("Enter another fruit (>Quit to see your plate): ").lower()
        else:
            same_orange += 1
            plate.append("Orange")
            fruit = input("Enter another fruit (>Quit to see your plate): ").lower()
    elif fruit == 'cherry':
        if same_cherry > 0:
            print(f"You've already put {fruit} on your plate.")
            fruit = input("Enter another fruit (>Quit to see your plate): ").lower()
        else:
            same_cherry += 1
            plate.append("Cherry")
            fruit = input("Enter another fruit (>Quit to see your plate): ").lower()
    elif fruit == 'kiwi':
        if same_kiwi > 0:
            print(f"You've already put {fruit} on your plate.")
            fruit = input("Enter another fruit (>Quit to see your plate): ").lower()
        else:
            same_kiwi += 1
            plate.append("Kiwi")
            fruit = input("Enter another fruit (>Quit to see your plate): ").lower()
    elif fruit == 'quit':
        print("Here is what on your plate:")
        for row in plate:
            print(row)
        print(f"""
The program terminated
Thanks for using!""")
        break
    else:
        print("I don't understand that.")
        fruit = input("Enter another fruit (>Quit to see your plate): ").lower()
