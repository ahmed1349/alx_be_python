# main-0.py
import sys
from bank_account import BankAccount

def main():
    # Initialize the BankAccount with an example starting balance of 100
    account = BankAccount(100)

    if len(sys.argv) < 2:
        # If insufficient arguments are passed
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    # Split the command and parameter from the argument
    command, *params = sys.argv[1].split(':')
    amount = float(params[0]) if params else None

    # Handle deposit command
    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: ${amount:.2f}")
    
    # Handle withdraw command
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: ${amount:.2f}")
        else:
            print("Insufficient funds.")
    
    # Handle display balance command
    elif command == "display":
        account.display_balance()
    
    else:
        # If the command is invalid
        print("Invalid command. Available commands: deposit, withdraw, display.")

if __name__ == "__main__":
    main()
