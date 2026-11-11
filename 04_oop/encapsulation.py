class BankAccount:
    def __init__(self, balance: float = 0.0) -> None:
        if balance < 0:
            raise ValueError("balance cannot be negative")
        self.__balance = balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("deposit must be positive")
        self.__balance += amount

    @property
    def balance(self) -> float:
        return self.__balance


if __name__ == "__main__":
    account = BankAccount(100)
    account.deposit(50)
    print(account.balance)
