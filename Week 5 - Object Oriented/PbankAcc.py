#make a program for a bank account
'''
Create an account

View balance

Deposit money

Withdraw money

Show account details
'''

class BankAccount: 
    def __init__(self,accountName,accountNumber, balance ):
        self.accountName = accountName
        self.accountNumber = accountNumber
        self.balance = balance
    
    def deposit(self, amount):
        if amount <= 0:
            print("Cannot deposit a negative or 0 amount!")
            return
        else:
            self.balance += amount
            print(f'{amount} deposited!')
    def withdraw(self, amount):
        if amount <= 0:
            print("Cannot withdraw a negative or 0 amount!")
            return
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f'{amount} withdrawed!')

    def view(self):
        print(f"Your balance is {self.balance}!")



johnAcc = BankAccount("John Doe", "123456789", 1000)
johnAcc.view()

johnAcc.deposit(500)
johnAcc.view()
johnAcc.withdraw(200)
johnAcc.view()
johnAcc.withdraw(1500) # Attempt to withdraw more than the balance
johnAcc.view()
johnAcc.deposit(-100)  # Attempt to deposit a negative amount
# Show account details
print(f"Account Name: {johnAcc.accountName}")
print(f"Account Number: {johnAcc.accountNumber}")
johnAcc.view()  # Final balance check













