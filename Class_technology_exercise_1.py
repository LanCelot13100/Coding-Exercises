# This program asks you to enter the character's name to show you it's stats
# Using 'class' technology :D
class Character:
    def __init__(self,health,damage,speed):
        self.health = health
        self.damage = damage
        self.speed = speed
Ninja = Character(50,90,100)
Viking = Character(100,100,40)
question = input("Enter any button to see characters' profiles: ")
print("""Here are the characters available to see their stats:
Ninja
Viking""")
question2 = input("Which one do you choose? ").lower()
while question2 == "ninja" or question2 == "viking" or len(question2) > 0:
    if question2 == "ninja":
        print(f"""Here is the table of Ninja's stats:
Health: {Ninja.health}
Damage: {Ninja.damage}
Speed: {Ninja.speed}""")
        question3 = input("")
        print("""The program terminated.
Thanks for using!""")
        break
    elif question2 == "viking":
        print(f"""Here is the table of Viking's stats:
Health: {Viking.health}
Damage: {Viking.damage}
Speed: {Viking.speed}""")
        question3 = input("")
        print("""The program terminated.
Thanks for using!""")
        break
    else:
        print("""I don't understand that.
Here are the characters available to see their stats:
Ninja
Viking""")
        question2 = input("Which one do you choose? ").lower()




