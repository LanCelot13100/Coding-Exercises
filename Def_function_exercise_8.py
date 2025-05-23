# This program is actually a copy of 'While_loop_exercise_8', but in this time I tried to make it word using 'def' functions
# If you're too lazy to go watch that, here is the description:

# Imagine that your have a car and you want to start it
# You start it and then you enter 'start' again, but the program tells you that you've already done that
# There is the same thing with the 'stop' command too
# If you try to stop the car before starting it, the program will tell you that you can't do that

# Was created using 'def' functions and booleans(True/False) :D

command = input("Enter 'start' to start the car or 'stop' to stop that: ").lower()
started = False
first_stop = True
stopped = False
while command:


    def start_command():
        return "You started the car!"

    def started_command():
        return "You've already started the car!"

    def stop_command():
        return "You stopped the car!"

    def stopped_command():
        return "You've already stopped the car! "

    def stop_first_command():
        return "You never started the car to stop that!"


    if command == 'start':
        if started:
            print(started_command())
            command = input("Enter 'start' to start the car or 'stop' to stop that (Q to quit): ").lower()
        else:
            started = True
            first_stop = False
            stopped = False
            print(start_command())
            command = input("Enter 'start' to start the car or 'stop' to stop that (Q to quit): ").lower()
    elif command == 'stop':
        if first_stop:
            print(stop_first_command())
            command = input("Enter 'start' to start the car or 'stop' to stop that (Q to quit): ").lower()
        elif stopped:
            print(stopped_command())
            command = input("Enter 'start' to start the car or 'stop' to stop that (Q to quit): ").lower()
        else:
            first_stop = False
            started = False
            stopped = True
            print(stop_command())
            command = input("Enter 'start' to start the car or 'stop' to stop that (Q to quit): ").lower()
    elif command == 'q':
        print("""The program terminated
Thanks for using!""")
        break
    else:
        print("I don't understand that...")
        command = input("Enter 'start' to start the car or 'stop' to stop that (Q to quit): ").lower()
