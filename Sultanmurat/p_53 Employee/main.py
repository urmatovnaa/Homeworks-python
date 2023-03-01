class Human:
    citizenship = 'Kyrgyzstan'
    def __init__(self, name, birthday, citizenship=None):
        self.name = name
        self.birthday = birthday
        self.citizenship = citizenship

    def info(self):
        return f'{self.name} was born in {self.birthday}, he is a citizen of {self.citizenship}'

    @classmethod
    def create_employee(cls, lst):
        name, birthday, citizenship, position, work_hour_day = lst
        return cls(name, birthday, citizenship), Employee(position, name, birthday, work_hour_day)

human1 = Human('Mura', '1995')
print(human1.info())

class Employee(Human):
    def __init__(self, position, name, birthday, work_hour_day=8):
        super().__init__(name, birthday)
        self.position = position
        self._work_hour_day = work_hour_day

    def __get_wage__(self):
        position_dict = {
            'chief': 350,
            'specialist': 250,
            'another': 150
        }
        return self._work_hour_day * position_dict[self.position]

    def __get_wage_month__(self, work_days):
        return work_days * self.__get_wage__()

    def get_wage_to_employee(self, passw):
        password = 2005
        if passw == password:
            return self.__get_wage_month__(15)
        else:
            print('Неверный пароль!')


human2 = Employee('chief', 'Sam', '1990')
print(human2.__get_wage__())
print(human2.__get_wage_month__(15))
print(human2.get_wage_to_employee(2005))

employee_info = ['Sofia', '2000', 'Kyrgyzstan', 'specialist', 8]
human3, employee = Human.create_employee(employee_info)
print(human3.info() + ', works as a ' + employee.position)
