# This email calculates the amount of vowels in the entered word
# If you enter more than 1 word, the program will tell you that
# Was created using 'def' function :D

word = input("Enter a word: ").lower()
vowels = "aouie"
while True:
    while " " in word:
        print("You need to enter only one word.")
        word = input("Enter a word: ").lower()


    def count_vowels():
        count = 0
        for row in word:
            if row in vowels:
                count += 1
        return count


    if int(count_vowels()) == 0:
        print("Looks like there are no vowels in this word.")
        word = input("Enter a word again (Q to quit): ").lower()
    elif int(count_vowels()) == 1:
        print(f"There is only {count_vowels()} vowel in this word.")
        word = input("Enter a word again (Q to quit): ").lower()
    elif int(count_vowels()) > 1:
        print(f"There are {count_vowels()} vowels in this word. ")
        word = input("Enter a word again (Q to quit): ").lower()
    if word == "q":
        print("""The program terminated
Thanks for using!""")
        break



