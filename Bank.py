import CheckingAccount
import SavingsAccount
import random


class Bank:
    def __init__(self, name: str):
        self.bankname = name

    def get_bank(self):
        print(self.bankname)

    @staticmethod
    def register_checking_account(name: str, bal):
        new_id = random.randint(100000000, 999999999)
        new_Account = CheckingAccount(name, new_id, name, bal)

    @staticmethod
    def register_savings_account(name: str, rate, bal, wlimit, tlimit):
        new_id = random.randint(100000000, 999999999)
        new_Account = SavingsAccount(name, new_id, name, bal, rate, wlimit, tlimit)
