from random import randrange


class BankAccount:
    def __init__(self):
        self.balance = 0
        self.account_id = randrange(100000, 199999)
        self.transactions_history = dict()

    def withdraw(self, sum_money):
        self.balance -= sum_money
        return self.balance

    def deposit(self, sum_money):
        self.balance += sum_money
        return self.balance

    def receive(self, sum_money, transfer_account):
        self.balance += sum_money
        if transfer_account in self.transactions_history:
            self.transactions_history[transfer_account].append(sum_money)
        else:
            self.transactions_history[transfer_account] = [sum_money, ]

    def transfer(self, sum_money, receiving_account):
        receiving_account.receive(sum_money, self.account_id)
        self.balance -= sum_money
        return f'Your balance {self.balance}'


bank_account_1 = BankAccount()
bank_account_1.deposit(100)
print(bank_account_1.__dict__, 00000)

bank_account_2 = BankAccount()
bank_account_1.receive(588, bank_account_2.account_id)
print(bank_account_1.__dict__)
bank_account_2.deposit(100)
print(bank_account_2.transfer(50, bank_account_1))
print(bank_account_2.__dict__)
print(bank_account_1.__dict__)
