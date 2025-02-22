
# Accounting Management System

## Introduction
The **Accounting Management System** is a Python-based console application designed to manage financial accounts and transactions efficiently. It provides features for adding, updating, and viewing accounts, recording transactions, and generating financial reports. The system follows **Object-Oriented Programming (OOP)** principles and implements essential data management techniques.

## Features
### **Admin Features:**
- Add new accounts with unique account IDs.
- View details of all accounts.
- Update existing account information.
- Record financial transactions (deposits and withdrawals).
- Generate financial reports, including account balances and transaction history.
- Check available balance for specific accounts.

## **System Components**
### **1. Account Management**
- Each account has an **ID, name, type (assets, liability, equity), and balance**.
- Supports updating of account details such as name, type, and balance.

### **2. Transactions**
- Allows recording **deposits and withdrawals**.
- Automatically updates the account balance after a transaction.

### **3. Reporting**
- **Account Balance Report:** Displays current balances of all accounts.
- **Transaction History Report:** Lists all transactions for a selected account.
- **Financial Summary Report:** Summarizes total assets, liabilities, and equity.

## **Technology Used**
- **Programming Language:** Python
- **Concepts Used:** Object-Oriented Programming (OOP), Data Structures (Lists, Encapsulation)

## **How to Run the Program**
1. Ensure you have **Python 3.x** installed.
2. Run the script using the command:
   ```bash
   python accounting_management.py
   ```
3. Follow the on-screen menu prompts to navigate through different functionalities.

## **Future Enhancements**
- Implement a **GUI using Tkinter or PyQt**.
- Add **database support (SQLite/MySQL)** for data persistence.
- Introduce **user authentication** for enhanced security.


