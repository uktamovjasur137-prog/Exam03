class BankAccount:
    def __init__(self, owner: str, balance: float):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float):
        if amount > 0:
            self.balance += amount
            print("Mablag muvaffaqiyatli qoshildi")
        else:
            print("Notogri summa")

    def withdraw(self, amount: float):
        if self.balance >= amount and amount > 0:
            self.balance -= amount
            print("Muvaffaqiyatli yechildi")
        else:
            print("Mablag yetarli emas")


bank1 = BankAccount("Jasur", 1000)

bank1.deposit(300)

print(bank1.balance)