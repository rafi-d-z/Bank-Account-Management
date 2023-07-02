import Account


class SavingsAccount(Account):
    def __init__(self, name: str, account_number: int, account_holder: str, balance, interest_rate,
                 withdrawal_limit: int, transfer_limit: int):
        super().__init__(name, account_number, account_holder, balance)
        self.rate = interest_rate
        self.wlimit = withdrawal_limit
        self.tlimit = transfer_limit

        self.transfers = 0

    # withdrawal limit is the limit in how much money you can withdraw at once
    def get_withdraw_limit(self):
        return self.wlimit

    # transfer limit is the limit in how many times you can withdraw from this account
    def get_transfer_limit(self):
        return self.tlimit

    def withdraw(self, withdraw_amt):
        if withdraw_amt < self.wlimit:
            if self.transfers < self.tlimit:
                self.bal -= withdraw_amt
            else:
                print("Transfer limit reached")
        else:
            print("Withdraw amount too high")

    def add_interest(self):
        self.bal = self.bal + self.bal * self.rate


