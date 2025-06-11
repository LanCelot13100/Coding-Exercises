#  This program sums the entered numbers up
#  Was created using 'Def' functions and *args

all_numbers = input("Enter numbers: ")

#  Here is the construction that indicates that there are ONLY integers in the list_numbers_2 which will be converted into a tuple later
list_numbers_2 = []
list_numbers = list(all_numbers)
print(list_numbers)
for row in list_numbers:
    row = int(row)
    list_numbers_2.append(row)


#  Here is the function that takes all numbers from list_numbers_2 and sums them all up
def sum_all_numbers(*numbers):
    total = 0
    for i in numbers:
        total += i
    return total
#  *numbers(args) is equal to list_numbers_2


print(f"Here is the addition of all entered numbers: {sum_all_numbers(*list_numbers_2)}")
