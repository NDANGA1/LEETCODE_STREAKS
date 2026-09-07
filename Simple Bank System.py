# Problem 2043: Simple Bank System
# You are to design a banking system that supports three main operations: transfer, deposit, and withdraw.
# The bank has n accounts numbered from 1 to n, with their initial balances stored in a 0-indexed array 'balance',
# where balance[i] represents the balance of account (i + 1).
#
# A transaction is valid only if:
# 1. The given account number(s) exist (1 <= account <= n).
# 2. The amount to withdraw or transfer does not exceed the account’s current balance.
#
# You must implement the Bank class with the following methods:
# - Bank(long[] balance): Initializes the bank with account balances.
# - boolean deposit(int account, long money): Adds 'money' to the given account if it exists.
# - boolean withdraw(int account, long money): Subtracts 'money' from the account if it exists and has enough funds.
# - boolean transfer(int account1, int account2, long money): Transfers 'money' from account1 to account2
#   if both accounts exist and account1 has sufficient funds.
#
# Example:
# Input:
# ["Bank", "withdraw", "transfer", "deposit", "transfer", "withdraw"]
# [[[10, 100, 20, 50, 30]], [3, 10], [5, 1, 20], [5, 20], [3, 4, 15], [10, 50]]
# Output:
# [null, true, true, true, false, false]
#
# Explanation:
# - Withdraw 10 from account 3 → success (new balance 10)
# - Transfer 20 from account 5 to 1 → success (account5=10, account1=30)
# - Deposit 20 to account 5 → success (account5=30)
# - Transfer 15 from account 3 to 4 → fail (insufficient funds)
# - Withdraw 50 from account 10 → fail (account doesn’t exist)
#
# Constraints:
# - 1 <= n, account, account1, account2 <= 10^5
# - 0 <= balance[i], money <= 10^12
# - At most 10^4 calls to each function


class Bank:

    def __init__(self, balance: List[int]):
        self.balance = balance

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if account1 <= len(self.balance) and account2 <= len(self.balance) and self.balance[account1 - 1] >= money:
            self.balance[account1 - 1] -= money
            self.balance[account2 - 1] += money
            return True
        else:
            return False

    def deposit(self, account: int, money: int) -> bool:
        if account <= len(self.balance):
            self.balance[account - 1] += money
            return True
        else:
            return False

    def withdraw(self, account: int, money: int) -> bool:
        if account <= len(self.balance) and self.balance[account - 1] >= money:
            self.balance[account - 1] -= money
            return True
        else:
            return False

# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)