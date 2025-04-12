
print("""Imagine that you're in a grocery store and you need to buy ONLY 3 groceries (Don't ask me why)
So this program inputs 3 prices of the picked groceries and sums them up!""")
question_1 = int(input("Enter the price of the first thing: "))
question_2 = int(input("Enter the price of the second thing: "))
question_3 = int(input("Enter the price of the third thing: "))
x = [question_1,question_2,question_3]
y = 0
for total in x:
    y += total
print(f"Total: {y}")