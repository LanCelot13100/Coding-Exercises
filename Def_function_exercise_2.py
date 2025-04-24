# This program asks to enter any three names and the united surname for entered names
# using 'def' function:D
first = input("Enter the first name: ")
second = input("Enter the second name: ")
third = input("Enter the third name: ")
surname = input("Enter the united surname for entered three names: ")
def name(fname):
    print(f'{fname} {surname}')
print("Here are three entered names with the united entered surname:")
name(first)
name(second)
name(third)
print("""The program has been terminated
Thanks for using!""")
