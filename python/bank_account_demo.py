from bank_account import BankAccount

account1=BankAccount("123", 100) #(account_number,balance)
print(account1) #Calls toString method

account1.deposit(50)
print(account1)

account1.withdraw(100)
print(account1)

account2=BankAccount("456",69)
print(account2)

account2.get_balance