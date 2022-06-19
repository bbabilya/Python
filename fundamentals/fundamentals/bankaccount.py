class BankAccount:
    users_list = []

    def __init__(self, int_rate = 0.01, balance = 0): 
        self.balance = balance
        self.int_rate = int_rate
        BankAccount.users_list.append(self)

    def deposit(self, amount):
        self.balance = self.balance + amount
        return self

    def withdraw(self, amount):
        self.balance = self.balance - amount
        return self

    def display_account_info(self):
        print("Balance:", self.balance)

    def yield_interest(self):
        if self.balance > 0:
            self.balance = (self.balance * self.int_rate) + self.balance
        return self
    
    @classmethod
    def display_all_info(cls):
        for user in cls.users_list:
            print("Balance:", user.balance)
            print("Interest Rate:", user.int_rate)


# fran = BankAccount(0.30, 3500)
# ema = BankAccount(0.10, 250)

# fran.deposit(200).deposit(200).deposit(200).withdraw(1000).yield_interest().display_account_info()

# ema.deposit(100).deposit(100).withdraw(10).withdraw(20).withdraw(15).withdraw(20).yield_interest().display_account_info()

# BankAccount.display_all_info()