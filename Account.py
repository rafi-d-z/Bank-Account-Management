import Bank


class Account(Bank):
    def __init__(self, name: str, account_number: int, account_holder: str, balance):
        super().__init__(name)
        self.accnum = account_number
        self.accholder = account_holder
        self.bal = balance

    def get_account_number(self):
        return self.accnum

    def get_account_holder(self):
        return self.accholder

    def withdraw(self, withdraw_amt):
        self.bal -= withdraw_amt

    def deposit(self, deposit):
        self.bal += deposit

    def check_bal(self):
        print(self.bal)
