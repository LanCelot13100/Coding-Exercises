# Here is the technology that just divides the 'x' variable into 3 numbers and adds the 'y' integer that you have to enter:
x = input("Numbers: ")
y = input("Added number: ")
first = x[0]
second = x[1]
third = x[2]
numbers = [int(first),int(second),int(third)]
for number in range(len(numbers)):
    numbers[number] += int(y)
    print(numbers[number])
