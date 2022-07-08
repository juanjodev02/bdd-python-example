from src.models.savingAccount import SavingAccount


class Client:
    def __init__(self, name: str, account: SavingAccount):
        self.name = name
        self.account = account
