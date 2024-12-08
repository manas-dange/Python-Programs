class BankAccount:
    def __init__(self, account_number, customer_name, balance, date_of_opening):
        self.account_number = account_number
        self.customer_name = customer_name
        self.balance = balance
        self.date_of_opening = date_of_opening

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit of {amount} successful. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawal of {amount} successful. New balance: {self.balance}")
        else:
            print("Insufficient balance or invalid amount.")
    def check_balance(self):
        return self.balance
    def print_account_details(self):
        print(f"Account Number: {self.account_number}")
        print(f"Customer Name: {self.customer_name}")
        print(f"Balance: {self.balance}")
        print(f"Date of Opening: {self.date_of_opening}")
account = BankAccount("123456789", "John Doe", 1000.0, "2023-01-01")
account.print_account_details()
account.deposit(500)
account.withdraw(200)
print(f"Current Balance: {account.check_balance()}")
