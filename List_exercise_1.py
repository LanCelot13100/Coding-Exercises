# Here is the program that was created using 'list' technology and also 'while' and 'for' loops!
# It asks you to enter 'start' and after that any five numbers that will be sorted later
# Also, this program determines the maximal and minimal numbers after sorting them
# Was created using lists :D
start = input("""Enter >start to start this program:
>""").lower()
while start == "start" or start == "q" or start:
    if start == "start":
        first = int(input("Enter the first number: "))
        second = int(input("Enter the second number: "))
        third = int(input("Enter the third number: "))
        forth = int(input("Enter the forth number: "))
        fifth = int(input("Enter the fifth number: "))
        list1 = [first,second,third,forth,fifth]
        list1.sort()
        min_number = list1[0]
        max_number = list1[4]
        print("Here is the list of all five entered numbers in the row:")
        for numbers in list1:
            print(numbers)
        print(f"The minimal number in this list is {min_number}")
        print(f"The maximal number in this list is {max_number}")
        start = input("""Enter >start to start this program again (Q to quit):
>""").lower()
    elif start == "q":
        print("""The program terminated
Thanks for using!""")
        break
    else:
        start = input("""Enter >start to start the program (Q to quit):
>""").lower()

