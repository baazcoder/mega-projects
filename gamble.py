import random

# Game constants
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1
ROWS = 3
COLS = 3

# Symbol configuration (symbol: count, value multiplier)
symbol_data = {
    "A": {"count": 2, "multiplier": 5},
    "B": {"count": 4, "multiplier": 3},
    "C": {"count": 6, "multiplier": 2},
    "D": {"count": 8, "multiplier": 1}
}

def deposit():
    """Get player deposit amount"""
    while True:
        amount = input("How much would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                return amount
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")

def get_number_of_lines():
    """Get number of lines to bet on"""
    while True:
        lines = input(f"Enter number of lines to bet on (1-{MAX_LINES}): ")
        if lines.isdigit():    
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                return lines
            else:
                print(f"Number of lines must be between 1 and {MAX_LINES}.")
        else:
            print("Please enter a number.")

def get_bet():
    """Get bet amount per line"""
    while True:
        bet = input(f"How much would you like to bet per line (${MIN_BET}-${MAX_BET})? $")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                return bet
            else:
                print(f"Bet must be between ${MIN_BET} and ${MAX_BET}.")
        else:
            print("Please enter a number.")

def spin_slot_machine():
    """Generate a spin result"""
    all_symbols = []
    for symbol, data in symbol_data.items():
        for _ in range(data["count"]):
            all_symbols.append(symbol)
    
    columns = []
    for _ in range(COLS):
        column = []
        current_symbols = all_symbols.copy()
        for _ in range(ROWS):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    
    return columns

def print_slot_machine(columns):
    """Display the slot machine result"""
    print("\nSlot Machine Result:")
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()  # New line after each row

def check_winnings(columns, lines, bet):
    """Calculate winnings based on spin result"""
    winnings = 0
    winning_lines = []
    
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += bet * symbol_data[symbol]["multiplier"]
            winning_lines.append(line + 1)
    
    return winnings, winning_lines

def play_round(balance):
    """Handle one round of slot machine play"""
    lines = get_number_of_lines()
    
    while True:
        bet = get_bet()
        total_bet = bet * lines
        
        if total_bet > balance:
            print(f"You don't have enough to bet that amount. Your current balance is: ${balance}")
        else:
            break
    
    print(f"\nYou are betting ${bet} on {lines} lines. Total bet: ${total_bet}")
    print(f"Current balance: ${balance - total_bet}")
    
    slots = spin_slot_machine()
    print_slot_machine(slots)
    
    winnings, winning_lines = check_winnings(slots, lines, bet)
    if winnings > 0:
        print(f"\n🎉 You won ${winnings}!")
        if winning_lines:
            print(f"Winning lines:", *winning_lines)
    else:
        print("\nSorry, you didn't win this time.")
    
    return winnings - total_bet

def main():
    """Main game loop"""
    print("\nWelcome to the Python Slot Machine!")
    print(f"Match symbols horizontally across {MAX_LINES} lines to win.")
    print("Symbol payouts:")
    for symbol, data in symbol_data.items():
        print(f"{symbol}: {data['multiplier']}x your bet")
    
    balance = deposit()
    
    while True:
        print(f"\nCurrent balance: ${balance}")
        if balance == 0:
            print("You're out of money! Game over.")
            break
        
        play = input("Press enter to play (q to quit): ").lower()
        if play == "q":
            break
        
        balance += play_round(balance)
    
    print(f"\nThank you for playing! You're leaving with ${balance}")

if __name__ == "__main__":
    main()