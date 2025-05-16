# Here is the program that is based on the technology that has been presented in 'For_loop_exercise_4'

numbers = input("Enter any 3 numbers: ")
while not (len(numbers) == 3 and numbers.isdigit()):
    if len(numbers) > 3 and numbers.isdigit() or len(numbers) < 3 and numbers.isdigit():
        print("You need to enter ONLY 3 numbers.")
        numbers = input("Enter any 3 numbers again: ")
    elif numbers.lstrip("-").isdigit():
        print("Numbers don't have to be negative.")
        numbers = input("Enter any 3 numbers: ")
    elif numbers.strip() == "":
        print("You didn't enter anything.")
        numbers = input("Enter any 3 numbers: ")
    elif not numbers.isdigit():
        print("You need to enter numbers.")
        numbers = input("Enter any 3 numbers again: ")
first_number = numbers[0]
second_number = numbers[1]
third_number = numbers[2]
numbers_list = [int(first_number),int(second_number),int(third_number)]
print(numbers_list)
plus_number = input("Enter a number that will be added to the entered 3 numbers: ")
while not (len(plus_number) == 1 and plus_number.isdigit()):
    if len(plus_number) > 1 and plus_number.isdigit():
        print("You need to enter only 1 number that will be added to the entered 3 numbers")
        plus_number = input("Enter a number that will be added to the entered 3 numbers again: ")
    elif len(plus_number) > 1 and plus_number.lstrip("-").isdigit():
        print("This number can't be negative.")
        plus_number = input("Enter a number that will be added to the entered 3 numbers again: ")
    elif plus_number.strip() == "":
        print("You didn't enter anything.")
        plus_number = input("Enter a number that will be added to the entered 3 numbers again: ")
    elif not plus_number.isdigit():
        print("You need to enter numbers.")
        plus_number = input("Enter a number that will be added to the entered 3 numbers again: ")
print("Here is the entered 3 numbers with another added number")
for number in range(len(numbers_list)):
    numbers_list[number] += int(plus_number)
    print(numbers_list[number])
print("""The program terminated
Thanks for using!""")
