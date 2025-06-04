#  This program is a copy of a the 'Martingale_System' project, but here it can automatically define tne the amount of steps to losing all your money
#  You just have to enter the amount of money that you have and the amount of money that you want to bet
#  By the way, now it has the boundaries like the minimal bet and the maximum one ;)
import random


#  This function return 'heads' or 'tails' using random module
def flip_coin():
    flip = random.randint(0,1)
    if flip == 0:
        return "heads"
    elif flip == 1:
        return "tails"



def martingale_tactic(*, current_money: int, current_bet: int, min_bet: int, max_bet: int) -> int:
    steps_to_loose = 0
    if current_bet > max_bet:
        current_bet = max_bet
        print(f"""Your bet can to be maximum 1000
So your current bet is {current_bet}""")
    elif current_bet < min_bet:
        current_bet = min_bet
        print(f"""Your bet has to be minimum 100
So your current bet is {current_bet}""")
    else:
        print(f"Your current bet is {current_bet}")

    while True:
        print("=================")
        if current_money > 0:
            steps_to_loose += 1
            current_money -= current_bet
            flip_flip = flip_coin()
            if flip_flip == "heads":
                current_money += (current_bet * 2)
                print("Won")
                print(current_money)
            else:
                current_bet *= 2
                print("loose")
                print(current_money)

        if current_money == 0:
            print("Game Over!")
            break
        elif current_money < 0:
            print("""Game Over!
You even got a debt :D""")
            break

    return steps_to_loose

money = int(input("Enter your money: "))
bet = int(input("Enter your bet (from 100 to 1000): "))
print(f"Here is the amount of tries that was done before losing all money: {martingale_tactic(current_money=money,current_bet=bet,min_bet=100,max_bet=1000)}")
