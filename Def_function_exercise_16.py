
#  Here is the program that filters the given numbers on even and odd ones
#  Was created using 'def' and 'filter' functions :D

number = int(input(f"Filter numbers on even and odd ones from 1 to "))
nums = range(1,number)


#  This function creates a list of even numbers from given ones
def even_numbers(numbers) -> list:
    new_numbers = []
    if numbers % 2 == 0:
        new_numbers.append(numbers)
        return new_numbers
#  The 'numbers' parameter is the 'nums' range


#  This function creates a list of odd numbers from given ones
def odd_numbers(numbers) -> list:
    new_numbers = []
    if numbers % 2 != 0:
        new_numbers.append(numbers)
        return new_numbers
#  The 'numbers' parameter is the 'nums' range


even_nums = list(filter(even_numbers,nums))
odd_nums = list(filter(odd_numbers,nums))
print(f"""Here id the list of the even numbers:
{even_nums}
And here is list of odd ones:
{odd_nums}""")
