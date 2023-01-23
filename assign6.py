import datetime

class BankAccount:
    def __init__(self, name, balance, account_type):
        self.name = name
        self.balance = balance
        self.account_type = account_type
        self.transactions = []
    
    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"{datetime.datetime.now()} - Deposited {amount}. New balance: {self.balance}")
        print(f"{amount} deposited. Current balance: {self.balance}")
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.transactions.append(f"{datetime.datetime.now()} - Withdrawn {amount}. New balance: {self.balance}")
            print(f"{amount} withdrawn. Current balance: {self.balance}")
        else:
            print("Insufficient balance.")
    
    def check_balance(self):
        print(f"Your current balance: {self.balance}")

    def check_transactions(self):
        for transaction in self.transactions:
            print(transaction)
            
class Bank:
    def __init__(self):
        self.accounts = {}
    
    def create_account(self, name, balance, account_type):
        account = BankAccount(name, balance, account_type)
        self.accounts[name] = account
        print(f"Account created for {name} with initial balance of {balance}")
    
    def check_account_exists(self, name):
        if name in self.accounts:
            return True
        else:
            return False
    
    def deposit(self, name, amount):
        if self.check_account_exists(name):
            self.accounts[name].deposit(amount)
        else:
            print(f"Account for {name} does not exist.")
            
    def withdraw(self, name, amount):
        if self.check_account_exists(name):
            self.accounts[name].withdraw(amount)
        else:
            print(f"Account for {name} does not exist.")
    
    def check_balance(self, name):
        if self.check_account_exists(name):
            self.accounts[name].check_balance()
        else:
            print(f"Account for {name} does not exist.")
    
    def check_transactions(self, name):
        if self.check_account_exists(name):
            self.accounts[name].check_transactions()
        else:
            print(f"Account for {name} does not exist.")
    
# Create a new bank
bank = Bank()

# Create a new bank account
name = input("Enter your name: ")
balance = int(input("Enter your initial balance: "))
account_type = input("Enter your account type (savings/current): ")
bank.create_account(name, balance, account_type)

while True:
   
