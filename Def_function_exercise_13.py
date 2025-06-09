#  This program defines the maximal number from the entered sequence
#  Was created using def functions and *args :D


#  Here is the function that can contain the infinite amount of numbers
#  It defines the maximal one from all of them
def find_max(*args):
    if args:
        x = list(args)
        x.sort()
        return x[-1]


numbers = input("Enter any amount numbers one by one with commas: ")

#  If the numbers were entered without commas, the program won't let you through
while not "," in numbers:
    print("You need to enter them with commas.")
    numbers = input("Enter any amount number one by one with commas again: ")


clean_list = numbers.split(",")
new_clean_list = []

#  Here we need to turn the entered numbers into integers, because they have been strings for the program until now
for i in clean_list:
    i = int(i)
    new_clean_list.append(i)

#  Later, we have to turn the 'new_clean_list' into a tuple and paste as an argument into the function with '*'
tuple_numbers = tuple(new_clean_list)
print(f"""Here is the maximal number from all entered ones: {find_max(*tuple_numbers)}

The program terminated
Thanks for using!""")

