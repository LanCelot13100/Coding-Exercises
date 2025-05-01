# Let's imagine that you have a car and you want to start it.
# You start it, but you got a thought like: "What if I enter 'start' again?"
# You enter 'start' again, BUT you this program tells you that "Hey, you've already started the car"
# This program has the same thing with the 'stop' command;
# So after every stop command, if you enter the 'start' command after that, the program has to restart and print "The car started"
# Created with a system of numbers (0 or 1)
started = 0
stopped = 1
command = input("""Enter the action:
>start (to start a car)
>stop (to stop a car)
>""").lower()
while command == "start" or command == "start" and started == 1 or command == "stop" or command == "stop" and stopped == 1 or len(command) > 0:
    if command == "start" and started == 1:
        command = input("""The car is already started!
Enter the action:
>start (to start a car)
>stop (to stop a car)
>""").lower()
    elif command == "start":
        started = 1
        stopped = 0
        command = input("""The car started.
Enter the action:
>start (to start a car)
>stop (to stop a car)
>""").lower()
    elif command == "stop" and stopped == 1:
        command = input("""The car is already stopped!
Enter the action:
>start (to start a car)
>stop (to stop a car)
>""").lower()
    elif command == "stop":
        stopped = 1
        started = 0
        command = input("""The car stopped.
Enter the action:
>start (to start a car)
>stop (to stop a car)
>""").lower()
    else:
        command = input("""I don't understand that...
Enter the action again:
>start (to start a car)
>stop (to stop a car)
>""").lower()



