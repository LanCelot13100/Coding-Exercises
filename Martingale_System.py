#  This program allows you see how much the martingale tactic in a gambling game ineffective on the heads & tails game
#  You just have to enter the amount of money that you have and the amount of money that you want to bet.

import random


#  This function return 'heads' or 'tails' using random module
def flip_coin():
    flip = random.randint(0,1)
    if flip == 0:
        return "heads"
    elif flip == 1:
        return "tails"


#  This function checks if the 'flip_coin()' function is equal to the side of the coin that you have bet on
#  If yes,then your current amount of money is being summed with the bet that you have bet
#  If no,then your current amount of money is being subtracted with the bet that you have bet
def remained_money_function(*,remained_money: int, bet_number: int, side_str: str, flip_flip: str):
    if flip_flip == side_str:
        remained_money = remained_money + (bet_number * 2)
        return remained_money
    elif flip_flip != side_str:
        remained_money = remained_money - bet_number
        return remained_money
#  The parameter 'remained_money' is your amount of money that you had before using the function and will have after using that (money)
#  The parameter 'bet_number' is your bet (bet)
#  The parameter 'side_str' is the side of the coin that you bet on (side)
#  The parameter 'flip_flip' is the 'flip_coin()' function


#  These are statuses that can be changed whether you won or failed
failed_status = "failed"
won_status = "won"
#  This function does actually the same thing that the 'remained_money_function' does, but here it returns the statuses that have been declared above this function
def result(*, won_result: str,failed_result: str, side_str: str, flip_flip: str):
    if flip_flip == side_str:
        return f"""You {won_result}!
Here is your remained money:"""
    elif flip_flip != side_str:
        return f"""You {failed_result}!
Here is your remained money:"""
#  The parameter 'won_result' is the 'won_status' variable (won_status)
#  The parameter 'failed_result' is the 'failed_status' variable (failed_status)
#  The parameter 'side_str' is the side of the coin that you bet on (side)
#  The parameter 'flip_flip' is the 'flip_coin()' function


#  This function returns the result of the main idea of the martingale tactic
#  Returns "failed"
def result_for_martingale_tactic(*, side_str: str, flip_flip: str):
    if flip_flip != side_str:
        return "failed"
#  The parameter 'side_str' is the side of the coin that you bet on (side)
#  The parameter 'flip_flip' is the 'flip_coin()' function


#  This function returns the bet that was multiplied with 2, after the failing
def martingale_tactic(*, martingale_bet: int):
    martingale_bet *= 2
    return martingale_bet
#  The parameter 'martingale_bet' is the bet that was multiplied with 2 (bet)


#  Here the input that asks you to enter the amount of money that you have
money = int(input("How much money do you have? "))
#  Here the input that asks you to enter the amount of money that you want to bet
bet = int(input("How much money do you want to bet? "))

while True:
    print("")
    current_bet = flip_coin()
    if current_bet == "heads":
        print(f"Here is the right side of the coin: Heads")
    else:
        print(f"Here is the right side of the coin: Tails")
    side = input("Which side do you want to bet on? ").lower()

    #  If the program doesn't understand you, it executes the while not loop down below
    while not (side == 'heads' or side == 'tails'):
        #  It says it doesn't understand you
        print("I don't understand.")
        if current_bet == "heads":
            print(f"Here is the right side of the coin: Heads")
        else:
            print(f"Here is the right side of the coin: Tails")
        side = input("Which side do you want to bet on? ").lower()

    # If the program understands you, it executes the functions with the arguments
    print(result(won_result=won_status, failed_result=failed_status, side_str=side, flip_flip=current_bet), remained_money_function(remained_money=money, bet_number=bet, side_str=side, flip_flip=current_bet))
    money = remained_money_function(remained_money=money, bet_number=bet, side_str=side, flip_flip=current_bet) #  The amount of money that you have after flipping the coin

    # If you fail, the 'martingale_tactic()' and 'result_for_martingale_tactic' functions execute
    if result_for_martingale_tactic(side_str=side, flip_flip=current_bet) == "failed":
        print(f"The current bet x2: {martingale_tactic(martingale_bet=bet)}")
        bet = martingale_tactic(martingale_bet=bet)
        if money <= 0:
            print("But your current bet doesn't matter anymore...")

    #  If your money is equal to 0 or less, the game is over for you and the program terminates, because the game is over for you :(
    if money <= 0:
        print("""
Because you are out of money now.
Game Over!""")
        break

