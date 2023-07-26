MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

def deposit():
    while True:
        amount = input("How much would you like to deposit? R")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than zero.")
        else:
            print("Please enter a number")

    return amount

def get_number_of_lines():
        while True:
            lines = input(f"How many lines would you like to best on each line? (1 - {str(MAX_LINES)})")
            if lines.isdigit():
                lines = int(lines)
                if 1 <= lines <= MAX_LINES:
                    break
                else:
                    print("Amount must be between 1 and 3")
            else:
                print("Please enter a number")

        return lines

def get_bet():
        while True:
            amount = input("How much would you like to bet? R")
            if amount.isdigit():
                amount = int(amount)
                if MIN_BET <= amount <= MAX_BET:
                    break
                else:
                    print(f"Amount must ne between R{MIN_BET} - R{MAX_BET}")
            else:
                print("Please enter a number")

        return amount

def main():
    balance = deposit()
    lines = get_number_of_lines()
    while True:
            bet = get_bet()
            total_bet = bet * lines

            if total_bet > balance:
                 print(f"You do not have enough money to bet that amount, your current balance is R{balance}")
            else:
                 break

    
    print(f"You are betting R{bet} on {lines} lines your total bet is R{total_bet}")


main()