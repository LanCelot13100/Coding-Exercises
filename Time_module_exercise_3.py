# Here is another way to make this stopwatch work :D
# In this time I used 'while' loop to get it done!
import time
start = input("Enter 'start' to start a stopwatch: ")
while not start == "start":
    print("I don't understand that.")
    start = input("Enter 'start' to start a stopwatch: ")
    print("The stopwatch has been started")
number = 0
while number < 59:
    time.sleep(1)
    number += 1
    print(number)
print("""The program terminated
Thanks for using!""")

