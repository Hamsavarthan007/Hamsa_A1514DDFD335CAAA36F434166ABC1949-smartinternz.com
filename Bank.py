class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance):
        self._account_number = account_number
        self._account_holder_name = account_holder_name
        self._account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self._account_balance += amount
            return f"Deposited ${amount}. New balance: ${self._account_balance}"
        else:
            return "Invalid deposit amount. Amount must be greater than 0."

    def withdraw(self, amount):
        if amount > 0 and amount <= self._account_balance:
            self._account_balance -= amount
            return f"Withdrew ${amount}. New balance: ${self._account_balance}"
        elif amount > self._account_balance:
            return "Insufficient funds for withdrawal."
        else:
            return "Invalid withdrawal amount. Amount must be greater than 0."

    def display_balance(self):
        return f"Account Balance for {self._account_holder_name}: ${self._account_balance}"


account = BankAccount("123456789", "John Doe", 1000.0)

print(account.display_balance())  
print(account.deposit(500))      
print(account.withdraw(200))  print(account.display_balance()) 

