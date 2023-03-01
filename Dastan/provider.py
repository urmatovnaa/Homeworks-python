# Напишите класс Subscriber, у которого есть переменные экземпляра:
# firstname
# lastname
class Subscriber:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

# Сделайте так, чтобы метод __repr__ возвращал firstname + lastname

    def __repr__(self):
        return f'{self.firstname} {self.lastname}'

# Напишите класс Provider, у которого есть:

class Provider:
    def __init__(self, name_of_providers):
        self.name = name_of_providers  # переменный экземпляра name -- название провайдера
        self.subscribers = list()  # переменный экземпляра subscribers -- список, в котором будут храниться экземпляры класса Subscriber
        self.payments = dict()  # переменный экземпляра payments -- словарь, ключём которого является экземпляр класса Subscriber,
# значением является сумма (вещественное число)

# метод register_payment, который принимает экземпляр класса Subscriber,
# и сумму, затем проверяет, есть ли такой экземпляр Subscriber в списке subscribers.
# Если есть, записывает экземпляр в словарь payments в качестве ключа, а сумму в качестве значения
# Если нет, выкидывает (raise) ошибку ValueError

    def register_payment(self, subscriber, sum_of_payment):
        if subscriber in self.subscribers:
            self.payments[subscriber] = sum_of_payment
        else:
            raise ValueError

# Напишите класс Terminal, у которого есть
# переменная экземпляра amount = 0
# переменная экземпляра providers = [ ]

class Terminal:
    def __init__(self):
        self.amount = 0
        self.providers = []

# Регистрировать провайдера через метод register, который принимает экземпляр класса Provider
# и добавляет в providers

    def register(self, provider):
        self.providers.append(provider)

# Принимать деньги в счет провайдера (pay), который принимает экземпляр класса Provider,
# экземпляр класса Subscriber и сумму (вещественное число).
# Внутри метода должен вызываться метод register_payment экземпляра класса Provider.
# register_payment успешно сработал, то в переменую amount нужно добавить сумму.

    def pay(self, provider, subscriber, sum_of_payment):
        provider.register_payment(subscriber, sum_of_payment)
        if register_payment is True:
            self.amount += sum_of_payment