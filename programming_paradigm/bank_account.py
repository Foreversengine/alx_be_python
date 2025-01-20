class BankAccount:
    def __init__(self, initial_balance=0):
        self.account_balance = initial_balance
    
    def deposit(self, amount):
        """Add the specified amount to the account balance."""
        if amount > 0:
            self.account_balance = amount + self.account_balance
        else:
            print("Amount cannot be a negative value!")
    def withdraw(self, amount):
        """Deduct the specified amount from the account balance if funds are sufficient."""
        if amount > 0 and self.account_balance >= amount:
            self.account_balance = self.account_balance - amount
            return True
        return False
    
    def display_balance(self):
        """Print the current balance in a user-friendly format."""
        print(f"Current Balance: ${self.account_balance:.2f}")