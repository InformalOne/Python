class Bank:

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, dep_amt):
        self.balance = self.balance + dep_amt
        print(f'added {dep_amt} to the balance')

    def withdraw(self, with_amt):
        if with_amt <= self.balance:
            self.balance = self.balance - with_amt
            print('withdrawal successful')

        else:
            print('sorry')

    def __str__(self):
        return f"owner: {self.owner}\n balance: {self.balance}"


a = Bank('Informal1', 100000)

print(a.withdraw(10000))
print(a.deposit(100000))
