from bankaccount import BankAccount

class User:
    users_list = []

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.account = BankAccount(int_rate=0.02, balance=0)
        User.users_list.append(self)

    def display_user_info(self):
        print("First Name:", self.first_name)
        print("Last Name:", self.last_name)
        print("Balance:", self.account.balance)
        return self
    
    def display_balance(self):
        print("Name:", self.first_name, self.last_name)
        print("Balance:", self.account.balance)
        return self

    def make_withdrawal(self, num):
        self.account.balance = self.account.balance - num
        return self

    def make_deposit(self, num):
        self.account.balance = self.account.balance + num
        return self

bob = User("Bob","Builder","Checking")




