import random
# После создания методов и переменных, попробуйте создать счет, пополнить баланс и снять деньги с баланса.
# После реализации этих методов, попробуйте создать несколько счетов,
# попробуйте совершить несколько денежных переводов.

# Создайте класс BankAccount, у которого должны быть:
class BankAccount:
    def __init__(self): # переменные объекта
        self.balance = 0 # balance (со значением 0 по умолчанию)
        self.account_id = random.randrange(100000, 199999) # account_id (со значением random.randrange(100000,199999))
        self.transactions_history = {} # transactions_history (c пустым словарем)
# методы
# withdraw (снять) принимает сумму, которую нужно снять с баланса и возвращает остаток баланса после снятия
    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

# deposit (положить) принимает сумму, которую нужно положить на баланс и возвращает остаток баланса после
# пополнения

    def deposit(self, sum):
        self.balance += sum
        return self.balance

# В созданный класс BankAccount добавьте методы: receive (принять) который принимает сумму,
# увеличивает свой баланс, записывает счет отправителя в словарь transactions_history в качестве ключа,
# и сумму добавляет в список, который является значением.
# Почему список? Потому что переводов от данного банковского счета может быть много
# (пока дату перевода не будем записывать)

    def receive(self, sum, account_id):
        self.balance += sum
        if account_id not in self.transactions_history:
            self.transactions_history[account_id] = [sum]
        else:
            self.transactions_history[account_id].append(sum)


# transfer (перевести), который принимает сумму и другой экземпляр класса BankAccount
# (параметр назовём receiving_account), на который нужно перевести деньги.
# В результате работы этого метода нужно уменьшить сумму на балансе,
# вызвать метод receive у receiving_account. Метод должен возвращать остаток денег на балансе после перевода.

    def transfer(self, sum, receiving_account):
        self.balance -= sum
        receiving_account.receive(sum, receiving_account)
        return self.balance


altynai = BankAccount()
osmon= BankAccount()
altynai.receive(2000, osmon.account_id)
altynai.transfer(1000, osmon)
altynai.receive(3000, osmon.account_id)
altynai.transfer(1000, osmon)
print(altynai.__dict__)
print(osmon.__dict__)