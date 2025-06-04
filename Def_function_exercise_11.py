# This program calculates the difference between the comfortable for you temperature and the temperature in the room
# Was created using 'def' functions :D

comfortable_temperature = int(input("Enter the comfortable temperature for you: "))
current_temperature = int(input("Enter the temperature in the room: "))


def temperature(*,room_temperature: int, needed_temperature: int) -> int:
    if room_temperature > needed_temperature:
        return room_temperature - needed_temperature
    elif room_temperature < needed_temperature:
        return needed_temperature - room_temperature


while True:
    if current_temperature == comfortable_temperature:
        print("There is no difference between this and that!")
        current_temperature = int(input("Enter the temperature in the room again: "))
    else:
        print(f"Here is the difference between the needed temperature and the entered one: {temperature(room_temperature=current_temperature, needed_temperature=comfortable_temperature)}")
        comfortable_temperature = int(input("Enter the comfortable temperature for you again: "))
        current_temperature = int(input("Enter the temperature in the room again: "))


