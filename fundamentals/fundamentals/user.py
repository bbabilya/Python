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
    
    # def transfer_money(self,other_user,amount):
    #     self.account.balance = self.account.balance - amount
    #     other_user.account.balance += amount
    #     return self


# miles = User("Miles", "Edgeworth", 5000)
# maya = User("Maya", "Fey", 100)
# phoenix = User("Phoenix", "Wright", 15)

# miles.make_deposit(12).make_deposit(20).make_deposit(18).make_withdrawal(200).display_balance()

# maya.make_deposit(200).make_deposit(50).make_withdrawal(10).make_withdrawal(60).display_balance()

# phoenix.make_deposit(10).make_withdrawal(100).make_withdrawal(100).make_withdrawal(100).display_balance()

# miles.transfer_money(phoenix,1000).display_balance()
# phoenix.display_balance()






