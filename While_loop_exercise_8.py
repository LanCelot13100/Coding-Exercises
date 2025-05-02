
# This is program is an addition to the previous one (While_loop_exercise_7.py)
# Here is the second variant of this program :D
# Created with booleans (True/False)
started = False
command = input("""Enter the action:
>start (to start a car)
>stop (to stop a car)
>""").lower()
while command:
    if command == "start":
        if started:
            command = input("""The car is already started!
Enter the action:
>start (to start a car)
>stop (to stop a car)
>""").lower()
        else:
            started = True
            command = input("""The car started.
Enter the action:
>start (to start a car)
>stop (to stop a car)
>""").lower()
    elif command == "stop":
        if not started:
            command = input("""The car is already stopped!
Enter the action:
>start (to start a car)
>stop (to stop a car)
>""").lower()
        else:
            started = False
            command = input("""The car is stopped.
Enter the action:
>start (to start a car)
>stop (to stop a car)
>""").lower()
    elif len(command) > 0:
        command = input("""I don't understand that...
Enter the action again:
>start (to start a car)
>stop (to stop a car)
>""").lower()

