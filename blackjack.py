import random

MAX_BET = 500
MIN_BET = 10

COL = 6
ROW = 2

card_count = {
    "A" : 4,
    "2" : 4,
    "3" : 4,
    "4" : 4,
    "5" : 4,
    "6" : 4,
    "7" : 4,
    "8" : 4,
    "9" : 4,
    "10" : 4,
    "J" : 4,
    "Q" : 4,
    "K" : 4,
}

def get_dealing(rows, cols, cards):
    all_cards = []
    for card, card_count in cards.item():
        for _ in range(card_count):
            all_cards.append(card)
    
    columns = []
    for _ in range(cols):
        column = []
        current_cards = all_cards[:]#copying the lsit
        for _ in range(rows):
            value = random.choice(all_cards)
            current_cards.remove(value)
            columns.append(column)

    return columns

def print_dealing(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row])
        

def game(balance):
    while True:
        bet = get_bet()
        if bet > balance:
            print(f"You do not have enough to bet, your balance is ${balance}")
        else: 
            break
    
    delt = get_dealing(ROW, COL, card_count)
    print_dealing(delt)


def deposit():
    while True:
        balance = input("Enter amount to deposit: $")
        if balance.isdigit():
            balance = int(balance)
            if balance > 0:
                break
            else:
                print("Enter a number greater than zero")
        else:
            print("Enter a number")
    return balance

def get_bet():
    while True:
        bet = input("How much do you want to wager? $")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Invalid amount to bet, enter an amount between ${MIN_BET} and ${MAX_BET}")
        else:
            print("Enter a number to bet")
    return bet



def main():
    depo = deposit()
    while True:
        print(f"Current balance is ${depo}")
        answer = input("Press enter to play (q to quit). ")
        if answer == 'q':
            break
        game(depo)

main()