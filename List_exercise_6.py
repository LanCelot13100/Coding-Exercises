#  This program is the advanced copy of 'List_exercise_2'
#  I decided to rewrite it just to check my progress out at programming :D

def validation(*,item: str, the_list: list, index: int) -> None:

    while not item.capitalize() == the_list[index]:
        print("It's the right fruit!")
        item = input("Enter the fruit again: ").capitalize()


fruits = ["Apple","Banana","Plum"]
print(fruits)

first = input("Enter the first fruit from the list: ")
validation(item=first,the_list=fruits,index=0)

second = input("Enter the second fruit from the list: ")
validation(item=second,the_list=fruits,index=1)

third = input("Enter the third fruit from the list: ")
validation(item=third,the_list=fruits,index=2)

print("""My congrats! You entered all fruits right!

The program terminated
Thanks for using!""")
