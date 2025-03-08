class BankAccount:
    def __init__(self,account_number,account_holder_name,balance):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.balance = balance
    
    def deposit(self,amount):
        self.balance += amount
        return self.balance
    
    def withdraw(self,amount):
        if amount > self.balance:
            return 'Insufficient balance'
        self.balance -= amount
        return self.balance
        
    def display_balance(self):
        return self.balance



acc1 = BankAccount("123456", "Alice", 500)
print(acc1.deposit(200))
print(acc1.withdraw(100))
print(acc1.display_balance())  
