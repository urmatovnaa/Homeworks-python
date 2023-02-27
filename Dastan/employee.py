# 1. Создайте класс Human a. Создайте метод __init__() и определите внутри него два динамических атрибута:
# name и birth_year (год рождения). Свои начальные значения они получают из параметров метода __init__()
# b. Определите внутри класса статический атрибут citizenship (гражданство) и укажите значение ‘Кыргызстан’.
# c. Создайте метод info () в котором будет возвращаться через return информация о человеке формата:
# «Нурсултан 1994 года рождения, гражданин Кыргызстана»
#
# 2. Создайте класс Employee (Сотрудник), который наследуется от класса Human a. Добавьте ему 2 динамических поля (атрибут)
# i. Первое поле position (должность) должно быть public так как такая информация как должность сотрудника она открытая и не является тайной,
# ii. Второе поле work_hours_day (количество рабочих часов в день) должно быть protected, так как мы не хотим,
# чтобы кто-то поменял количество рабочих часов в день у сотрудника
# b. Используя нижеописанную таблицу создайте private метод get_wage () которая будет возвращать через return заработную плату за день,
# и мы не хотим, чтобы кто-то смог получить доступ к заработной плате сотрудника, это коммерческая тайна.

class Human:
    def __init__(self, name, birth_year, citizenship='Кыргызстан'):
        self.name = name
        self.birth_year = birth_year
        self.citizenship = citizenship

    def info(self):
        return f'{self.name} {self.birth_year} года рождения, гражданин {self.citizenship}'

class Employee(Human):
    def __init__(self, name, birth_year, position, work_hours_day, citizenship):
        self.position = position
        self._work_hours_day = work_hours_day
        super().__init__(name, birth_year, citizenship)

    def __get_wage(self, _work_hours_day):
        wage_rate = {'chief': 350, 'specialist': 250, 'another': 150}
        for k, v in wage_rate.items():
            if self.position == k:
                return v * _work_hours_day


    def __get_wage_month(self, work_days):
        return self.__get_wage * work_days


    def get_wage_to_employee(self, work_days, password):
        entry_code = 12345
        if password == entry_code:
            return self.__get_wage(work_days)
        else:
            return "Неверно введен пароль"

    @classmethod
    def create_employee(cls, list_1):
        return cls(name= list_1[0], birth_year=list_1[1], position=list_1[2], work_hours_day= list_1[3], citizenship=list_1[4])

    def info(self):
        return f'{self.name} {self.birth_year} года рождения, гражданство {self.citizenship}, работает в должности {self.position}»'






dastan = Employee('Dastan', 1992,'chief', 12,'england')
print(dastan.info())