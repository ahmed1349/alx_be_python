# bank_account.py
class BankAccount:
    def __init__(self, initial_balance=0):
        # Initialize the account balance with an optional initial balance (default is 0)
        self.account_balance = initial_balance

    def deposit(self, amount):
        """Deposit the specified amount to the account balance."""
        if amount > 0:
            self.account_balance += amount
        else:
            print("Amount must be positive.")

    def withdraw(self, amount):
        """Withdraw the specified amount from the account balance if sufficient funds exist."""
        if amount > 0 and amount <= self.account_balance:
            self.account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        """Display the current account balance."""
        print(f"Current Balance: ${self.account_balance:.2f}")
