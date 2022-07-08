class SavingAccount:
    def __init__(self, balance):
        self.balance = balance

    def transfer(self, amount: float, destination) -> None:
        # check if amount is greater than balance
        if amount > self.balance:
            raise ValueError("Amount greater than balance, aborting transfer")
        # transfer amount
        self.balance -= amount
        destination.balance += amount
