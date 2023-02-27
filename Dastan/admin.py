class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        return self.restaurant_type, self.restaurtant_name

    def open_restaurant(self):
        print("Ресторан открыт")

    def set_number_served(self, count):
        self.number_served = count

    def increment_number_served(self, count):
        self.number_served += count


class User:
    def __init__(self, first_name, last_name, age, login_attempts):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attempts = login_attempts

    def describe_user(self):
        print(self.first_name, self.last_name, self.age)

    def greet_user(self):
        print(f'Hello {self.first_name}')

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


# Киоск с мороженым: киоск с мороженым — особая разновидность ресторана .
# Напишите класс IceCreamStand, наследующий от класса Restaurant из предыдущего упражнения.
# Добавьте атрибут с именем flavors для хранения списка сортов мороженого .
# Напишите метод, который выводит этот список . Создайте экземпляр IceCreamStand и вызовите этот метод.
# Администратор: администратор — особая разновидность пользователя .



class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors):
        self.flavors = flavors
        super().__init__(restaurant_name, cuisine_type)

    def info_flavors(self):
        return 'Есть следующие вкусы: '+', '.join(self.flavors)

# Напишите класс с именем Admin, наследующий от класса User из предыдущего упражнения.
# Добавьте атрибут privileges для хранения списка строк вида «разрешено добавлять сообщения»,
# «разрешено удалять пользователей», «разрешено банить пользователей» и т . д .
# Напишите метод show_privileges() для вывода набора привилегий администратора .
# Создайте экземпляр Admin и вызовите свой метод .

class Admin(User):
    def __init__(self, first_name, last_name, age, login_attempts):
        self.privileges = ['«разрешено добавлять сообщения', 'разрешено удалять пользователей',
                           'разрешено банить пользователей']
        super().__init__(first_name, last_name, age, login_attempts)

    def show_privileges(self):
        print(self.privileges)

# Привилегии: напишите класс Privileges .
# Класс должен содержать всего один атрибут privileges со списком строк из упражнения выше.
# Переместите метод show_privileges() в этот класс .
# Создайте экземпляр Privileges как атрибут класса Admin .
# Создайте новый экземпляр Admin и используйте свой метод для вывода списка привилегий .

class Privileges:
    def __init__(self):
        self.privileges = ['«разрешено добавлять сообщения', 'разрешено удалять пользователей',
                           'разрешено банить пользователей']

    def show_privileges(self):
        print(self.privileges)