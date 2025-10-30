class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance!")

    def display(self):
        print(f"Account holder: {self.name}")
        print(f"Balance: ₹{self.balance}")

# Example usage
acc = BankAccount("Soumen", 5000)
acc.deposit(1500)
acc.withdraw(2000)
acc.display()
