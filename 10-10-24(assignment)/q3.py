'''
Create an abstract class BankAccount with methods deposit(), withdraw(), and get_balance(). Then, create two subclasses:

SavingsAccount, where the withdraw() method ensures that the balance cannot go below $500.
CurrentAccount, where the withdraw() method allows the balance to go negative (up to $1000 overdraft).
Ensure that only deposit() and withdraw() are exposed to the user, and the balance is encapsulated (hidden).
'''

# from abc import ABC, abstractmethod

# # Abstract class BankAccount
# class BankAccount(ABC):
#     def __init__(self, initial_balance=0):
#         self._balance = initial_balance 

#     @abstractmethod
#     def deposit(self, amount):
#         pass

#     @abstractmethod
#     def withdraw(self, amount):
#         pass

#     def get_balance(self):
#         return self._balance

# # SavingsAccount class with a minimum balance restriction
# class SavingsAccount(BankAccount):
#     def deposit(self, amount):
#         if amount > 0:
#             self._balance += amount
#             print(f"Deposited ${amount}. New balance is ${self._balance}.")
#         else:
#             print("Deposit amount must be positive.")

#     def withdraw(self, amount):
#         if amount > 0:
#             if self._balance - amount >= 500:
#                 self._balance -= amount
#                 print(f"Withdrew ${amount}. New balance is ${self._balance}.")
#             else:
#                 print("Insufficient funds. Savings Account must maintain a minimum balance of $500.")
#         else:
#             print("Withdrawal amount must be positive.")

# # CurrentAccount class with an overdraft limit
# class CurrentAccount(BankAccount):
#     def deposit(self, amount):
#         if amount > 0:
#             self._balance += amount
#             print(f"Deposited ${amount}. New balance is ${self._balance}.")
#         else:
#             print("Deposit amount must be positive.")

#     def withdraw(self, amount):
#         if amount > 0:
#             if self._balance - amount >= -1000:
#                 self._balance -= amount
#                 print(f"Withdrew ${amount}. New balance is ${self._balance}.")
#             else:
#                 print("Insufficient funds. Overdraft limit reached.")
#         else:
#             print("Withdrawal amount must be positive.")

# # Usage
# savings = SavingsAccount(1000)
# current = CurrentAccount(500)

# # Test SavingsAccount
# savings.deposit(200)  # Should increase balance
# savings.withdraw(700)  # Should succeed
# savings.withdraw(600)  # Should fail due to minimum balance constraint

# # Test CurrentAccount
# current.deposit(300)  # Should increase balance
# current.withdraw(1000)  # Should succeed
# current.withdraw(800)  # Should fail due to overdraft limit


