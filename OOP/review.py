class BankAccount:

    def __init__(self, account_balance = 3000):
        self.account_balance = account_balance

    def show_balance(self):
        return self.account_balance