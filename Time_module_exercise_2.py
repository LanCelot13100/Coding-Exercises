# Here is my stopwatch that I created using 'time' module
import time
start = input("Enter 'start' to start a stopwatch: ")
while not start == "start":
    print("I don't understand that.")
    start = input("Enter 'start' to start a stopwatch: ")
    print("The stopwatch has been started")
for line in range(1,60):
    time.sleep(1)
    print(line)
print("""The program terminated
Thanks for using!""")


