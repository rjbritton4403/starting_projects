import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A" : 2,
    "B" : 4,
    "C" : 6,
    "D" : 8
}
symbol_value = {
    "A" : 5,
    "B" : 4,
    "C" : 3,
    "D" : 2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winnings_lines = []
    for line in range(lines):#looping through every row that the user bet on (lines)
        symbol = columns[0][line]#0 element at the current line, checking the first symbol in the column
        for column in columns:#looping through every column and checking to see if the symbol is there
            symbol_to_check = column[line]#symbol to check is the column at the current row we are looking at
            if symbol != symbol_to_check:# if symbols are not the same then the loop breaks
                break
        else:#for else statment for if the for loop does not break
            winnings += values[symbol] * bet#the value of that symbol multiplied by the bet
            winnings_lines.append(line + 1)#current line number 
    
    return winnings, winnings_lines

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():#.items gives key and value in dictionary
        for _ in range(symbol_count):
            all_symbols.append(symbol)#adding values from symbol count to all_symbols
    
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]#copying the list
        for _ in range(rows):#for every column we generate symbols for each column
            value = random.choice(all_symbols)
            current_symbols.remove(value)#find the first instance of the value in the list and remove it
            column.append(value)

        columns.append(column)

    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):#looping every row
        for i, column in enumerate(columns):#for every single row you loop through a column
            if i != len(columns) - 1:
                print(column[row], end=" | ")#print the current row that you are on 
            else:
                print(column[row], end="")#end tells the print statment what to end the line on
        print()

def deposit():#collecting user input for the deposit
    while True:
        amount = input("Enter a depoit amount: $")
        if amount.isdigit():#verifys if amount is a number
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")
    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter amount of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():#verifys if lines is a number
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines")
        else:
            print("Please enter a number.")
    return lines

def get_bet():
    while True:
        amount = input("How much would you like to bet on each line? $")
        if amount.isdigit():#verifys if amount is a number
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Enter a valid number to bet between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number.")
    return amount

def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"You do not have enough to bet that amount, your balance is: ${balance}")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines. Total bet is: ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winnging_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print(f"You won on lines:", *winnging_lines)
    return winnings - total_bet#return how much the user won or lost

def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play (q to quit).")
        if answer == 'q':
            break
        balance += spin(balance)#updating balance based on the spin

    print(f"You left with ${balance}")


   

main()