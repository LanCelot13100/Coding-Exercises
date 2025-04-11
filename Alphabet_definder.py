print("This is the English alphabet:")
print("abcdefghijklmnopqrstuvwxyz")
print("")
z = input("Do you want to receive a letter in the word or a number of the letter in the word? ")
while z == "Letter" or z == "letter" or z == "Number" or z == "number" or len(z) > 0:
    if z == "letter" or z == "Letter":
        text = input("Enter any word: ")
        q = input("Enter any letter in this word: ")
        if q in text:
            alphabet = "abcdefghijklmnopqrstuvwxyz"
            x = alphabet.find(q.lower())
            print("The number of this letter in the alphabet is " + str(x))
            break
        else:
            print("Looks like you've entered the wrong letter...")
            q = input("Enter any letter in this word again: ")
            while q in text or q not in text:
                if q in text:
                    alphabet = "abcdefghijklmnopqrstuvwxyz"
                    x = alphabet.find(q.lower())
                    print("The number of this letter in the alphabet is " + str(x))
                    break
                else:
                    print("Looks like you've entered the wrong letter...")
                    q = input("Enter any letter in this word again: ")

    elif z == "Number" or z == "number":
        text = input("Enter any word: ")
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        q = input("Enter any number of the letter in this word: ")
        x = alphabet.find(text[int(q)])
        print(x)
    else:
        print("Looks like you've entered the wrong letter...")
        z = input("Letter or Number? ")

