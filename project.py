'''
PROJECT TITLE: Accounting Management System
THIS PROJECT IS PROGRAMMED BY 
NAME:IRUM IMTIAZ                   
REG.NO: FA22-BCT-011          
'''

class Account:
    def __init__(self, account_id, account_name, account_type, balance=0):
        self.__account_id = account_id
        self.__account_name = account_name
        self.__account_type = account_type
        self.__balance = balance

    def get_account_id(self):
        return self.__account_id

    def get_account_name(self):
        return self.__account_name

    def get_account_type(self):
        return self.__account_type

    def get_balance(self):
        return self.__balance

    def set_account_name(self, account_name):
        self.__account_name = account_name

    def set_account_type(self, account_type):
        self.__account_type = account_type

    def set_balance(self, balance):
        self.__balance = balance

    def add_account(self):
        print(f"Account {self.__account_id} added with balance {self.__balance}")

    def update_account(self):
        print(f"Account {self.__account_id} updated with name {self.__account_name} and type {self.__account_type}")

    def check_balance(self):
        print(f"Account balance for {self.__account_id}: {self.__balance}")
        return self.__balance

class Transaction:
    def __init__(self, transaction_id, date, amount, transaction_type, account):
        self.__transaction_id = transaction_id
        self.__date = date
        self.__amount = amount
        self.__transaction_type = transaction_type
        self.__account = account

    def get_transaction_id(self):
        return self.__transaction_id

    def get_date(self):
        return self.__date

    def get_amount(self):
        return self.__amount

    def get_transaction_type(self):
        return self.__transaction_type

    def get_account(self):
        return self.__account

    def set_date(self, date):
        self.__date = date

    def set_amount(self, amount):
        self.__amount = amount

    def set_transaction_type(self, transaction_type):
        self.__transaction_type = transaction_type

    def set_account(self, account):
        self.__account = account

    def record_transaction(self):
        print(f"Recording transaction {self.__transaction_id}: {self.__amount} on {self.__date} ({self.__transaction_type}) for account {self.__account.get_account_id()}")

    def update_account_balance(self):
        if self.__transaction_type == "deposit":
            self.__account.set_balance(self.__account.get_balance() + self.__amount)
        elif self.__transaction_type == "withdrawal":
            self.__account.set_balance(self.__account.get_balance() - self.__amount)
        print(f"Updated account balance: {self.__account.get_balance()}")



    
    
def main_menu():
    accounts = []
    transactions = []

    print("*************************************************************************************************************************************** ")
    print("                                   WELCOME TO Accounting Management System                                            ")
    print(" ")
    print("*************************************************************************************************************************************** ")
    print(" ")
    
    while True:
        print("\nMain Menu")
        print("1. Add Account")
        print("2. View Accounts")
        print("3. Add Transaction")
        print("4. View Transactions")
        print("5. Check Account Balance")
        print("6. Update Account")
        print("7. Generate Reports")
        print("8. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_account(accounts)
        elif choice == '2':
            view_accounts(accounts)
        elif choice == '3':
            add_transaction(accounts, transactions)
        elif choice == '4':
            view_transactions(transactions)
        elif choice == '5':
            check_account_balance(accounts)
        elif choice == '6':
            update_account(accounts)
        elif choice == '7':
            generate_reports(accounts, transactions)
        elif choice == '8':
            break
        else:
            print("Invalid choice. Please try again.")

def update_account(accounts):
    if not accounts:
        print("No accounts available. Please add an account first.")
        return
    
    account_id = input("Enter account ID to update: ")
    for account in accounts:
        if account.get_account_id() == account_id:
            new_name = input("Enter new account name: ")
            new_type = input("Enter new account type: ")
            new_balance = float(input("Enter new balance: "))
            
            # Update the account details
            account.set_account_name(new_name)
            account.set_account_type(new_type)
            account.set_balance(new_balance)
            
            print("Account updated successfully.")
            return
    
    print("Account not found with the given ID.")

def add_account(accounts):
    account_id = input("Enter account ID: ")
    account_name = input("Enter account name: ")
    account_type = input("Enter account type(assets,liability,equity): ")
    balance = float(input("Enter initial balance: "))
    
    account = Account(account_id, account_name, account_type, balance)
    accounts.append(account)
    account.add_account()

def view_accounts(accounts):
    if not accounts:
        print("No accounts available.")
    else:
        for account in accounts:
            print(f"ID: {account.get_account_id()}, Name: {account.get_account_name()}, Type: {account.get_account_type()}, Balance: {account.get_balance()}")

def add_transaction(accounts, transactions):
    if not accounts:
        print("No accounts available. Please add an account first.")
        return
    
    transaction_id = input("Enter transaction ID: ")
    date = input("Enter transaction date: ")
    amount = float(input("Enter amount: "))
    transaction_type = input("Enter transaction type (deposit/withdrawal): ")
    
    print("Available Accounts:")
    for i, account in enumerate(accounts):
        print(f"{i+1}. {account.get_account_name()} (ID: {account.get_account_id()})")
    
    account_index = int(input("Select account by number: ")) - 1
    
    if 0 <= account_index < len(accounts):
        account = accounts[account_index]
        transaction = Transaction(transaction_id, date, amount, transaction_type, account)
        transactions.append(transaction)
        transaction.record_transaction()
        transaction.update_account_balance()
    else:
        print("Invalid account selection.")

def view_transactions(transactions):
    if not transactions:
        print("No transactions available.")
    else:
        for transaction in transactions:
            print(f"ID: {transaction.get_transaction_id()}, Date: {transaction.get_date()}, Amount: {transaction.get_amount()}, Type: {transaction.get_transaction_type()}, Account: {transaction.get_account().get_account_name()}")

def check_account_balance(accounts):
    if not accounts:
        print("No accounts available. Please add an account first.")
        return
    
    print("Available Accounts:")
    for i, account in enumerate(accounts):
        print(f"{i+1}. {account.get_account_name()} (ID: {account.get_account_id()})")
    
    account_index = int(input("Select account by number: ")) - 1
    
    if 0 <= account_index < len(accounts):
        accounts[account_index].check_balance()
    else:
        print("Invalid account selection.")

def generate_reports(accounts, transactions):
    while True:
        print("\nReports Menu")
        print("1. Generate Account Balance Report")
        print("2. Generate Transaction History Report")
        print("3. Generate Financial Summary Report")
        print("4. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == '1':
            generate_account_balance_report(accounts)
        elif choice == '2':
            generate_transaction_history_report(accounts, transactions)
        elif choice == '3':
            generate_financial_summary_report(accounts, transactions)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

def generate_account_balance_report(accounts):
    if not accounts:
        print("No accounts available.")
    else:
        print("\nAccount Balance Report")
        for account in accounts:
            print(f"ID: {account.get_account_id()}, Name: {account.get_account_name()}, Balance: {account.get_balance()}")

def generate_transaction_history_report(accounts, transactions):
    if not accounts:
        print("No accounts available.")
        return
    
    print("Available Accounts:")
    for i, account in enumerate(accounts):
        print(f"{i+1}. {account.get_account_name()} (ID: {account.get_account_id()})")
    
    account_index = int(input("Select account by number: ")) - 1
    
    if 0 <= account_index < len(accounts):
        account = accounts[account_index]
        print(f"\nTransaction History Report for Account ID: {account.get_account_id()}, Name: {account.get_account_name()}")
        for transaction in transactions:
            if transaction.get_account() == account:
                print(f"ID: {transaction.get_transaction_id()}, Date: {transaction.get_date()}, Amount: {transaction.get_amount()}, Type: {transaction.get_transaction_type()}")
    else:
        print("Invalid account selection.")

def generate_financial_summary_report(accounts, transactions):
    if not accounts:
        print("No accounts available.")
        return

# Initialize variables to store total balances
    total_assets = 0
    total_liabilities = 0
    total_equity = 0

# Iterate through each account
    for account in accounts:
        # Get the account type in lowercase
        account_type = account.get_account_type().lower()
        
        # Check the account type and update the corresponding total balance
        if account_type == "asset":
            total_assets += account.get_balance()
        elif account_type == "liability":
            total_liabilities += account.get_balance()
        elif account_type == "equity":
            total_equity += account.get_balance()

    print("\nFinancial Summary Report")
    print(f"Total Assets: {total_assets}")
    print(f"Total Liabilities: {total_liabilities}")
    print(f"Total Equity: {total_equity}")

if __name__ == "__main__":
    main_menu()
