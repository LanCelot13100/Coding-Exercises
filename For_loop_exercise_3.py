# This program gives you even or odd numbers in the range of entered ones
# If the first number is less than the second one, the program will give you the sequence of them whether you want even or odd ones
# If the first number is more than the second one, the program will give you the reversed sequence of that.
# It can work with negative numbers either :D

first = input("Enter the first number: ")
while not first.lstrip("-").isdigit():
    print("You need to enter a number.")
    first = input("Enter the first number again: ")
second = input("Enter the second number: ")
while not second.lstrip("-").isdigit():
    print("You need to enter a number.")
    second = input("Enter the second number again: ")
remainder = input(f"""Do you want to see even or odd numbers in the range between {first} and {second} numbers?
>Even
>Odd
>""").lower()
while not (remainder == "even" and first > second or remainder == "even" and first < second or remainder == "odd" and first > second or remainder == "odd" and first < second):
    print("I don't understand that...")
    remainder = input("So even or odd ones? ")
if remainder == "even" and first < second:
    double_second = int(second) + 1
    range_ = range(int(first), int(double_second))
    print(f"Here is the list of even numbers between {first} and {second} numbers:")
    for row in range_:
        remainder1 = row % 2
        if remainder1 == 0:
            print(row)
    print("""The program terminated
Thanks for using!""")
elif remainder == "even" and first > second:
    double_second = int(second) + 1
    range_ = range(int(double_second) - 2, int(first) + 2)
    print(f"Here is the list of even numbers between {first} and {second} numbers:")
    for row in reversed(range_):
        remainder1 = row % 2
        if remainder1 == 0:
            print(row)
    print("""The program terminated
Thanks for using!""")
elif remainder == "odd" and first < second:
    double_second = int(second) + 1
    range_ = range(int(first), int(double_second))
    print(f"Here is the list of even numbers between {first} and {second} numbers:")
    for row in range_:
        remainder1 = row % 2
        remainder2 = row % 1
        if remainder2 == 0 and remainder1 != 0:
            print(row)
    print("""The program terminated
Thanks for using!""")
elif remainder == "odd" and first > second:
    double_second = int(second) + 1
    range_ = range(int(double_second) - 2, int(first) + 2)
    print(f"Here is the list of even numbers between {first} and {second} numbers:")
    for row in reversed(range_):
        remainder1 = row % 2
        remainder2 = row % 1
        if remainder2 == 0 and remainder1 != 0:
            print(row)
    print("""The program terminated
Thanks for using!""")


# odd numbers = 1,3,5,7,9
# even numbers = 2,4,6,8,10

