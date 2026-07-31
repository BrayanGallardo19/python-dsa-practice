class Wallet:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount  # Safely add to the balance

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount  # Safely remove from the balance

    def get_balance(self):
        return self.__balance  # Public method to access the private balance

# Example usage
wallet = Wallet(100)
wallet.deposit(50)
wallet.withdraw(30)
print(wallet.get_balance())  # Output: 120

#mismo ejemplo pero con metodo privado

class Wallet:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute

    def __validate(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        if amount > self.__balance:
            raise ValueError("Insufficient funds")
    def deposit(self, amount):
        self.__validate(amount)  # Validate the amount before depositing
        self.__balance += amount  # Safely add to the balance

    def withdraw(self, amount):
        self.__validate(amount)  # Validate the amount before withdrawing
        self.__balance -= amount  # Safely remove from the balance

    def get_balance(self):
        return self.__balance  # Public method to access the private balance

# Example usage
wallet = Wallet(100)
wallet.deposit(50)
wallet.withdraw(30)
print(wallet.get_balance())  # Output: 120
