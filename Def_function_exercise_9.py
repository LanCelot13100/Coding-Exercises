# This program calculates the arithmetic mean of the entered numbers
# Was created using 'def' functions :D

numbers = input("Enter some numbers: ")
numbers_list = []
for char in numbers:
    numbers_list.append(int(char))


def arithmetic_mean():
    count = 0
    for row in numbers_list:
        if row:
            count += row
    division = count / len(numbers_list)
    return division


print(arithmetic_mean())
