import Account


class CheckingAccount(Account):
    def __init__(self, name: str, account_number: int, account_holder: str, balance):
        super().__init__(name, account_number, account_holder, balance)
