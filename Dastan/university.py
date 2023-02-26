# Ниже представлены связанные задачи. Цель: создать симуляцию университета.
# Обратите внимание на методы add_department и add_student.
# Подумайте, как решить проблему перезаписи существующих в словаре данных.
# Создайте экземпляр университета. Создайте нескольких студентов. Добавьте факультеты.
# Добавьте студентов в факультеты.

# Создайте класс University. В конструкторе создайте переменную экземпляра name,
# куда записывается переданный аргумент university_name.
class University:
    def __init__(self, university_name,):
        self.name = university_name
        self.departments = {} # Создайте переменную класса departments, у которого значение по умолчанию -- пустой словарь

# Создайте метод add_department, у которого параметр название факультета.
# Метод должен записать в словарь departments название факультета, а в качестве значения -- пустой список
    def add_department(self, name_of_department):
        self.departments[name_of_department] = []
# Создайте метод add_student с параметрами название факультета и объект студент -- экземпляр класса Student.
# Метод должен записать в словарь departments студента в соответствующий факультет.

    def add_student(self, department_name, dastan):
        for k, v in self.departments.items():
            if k == department_name:
                v.append(dastan)
        print(self.departments)

# Создайте класс Student, в конструкторе которого записывается firstname, lastname студента.
# Т.е. при создании экземпляра должны быть переданы имя и фамилия студента.

class Student:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.fullname = f'{firstname} {lastname}'

    def __repr__(self):
        return self.fullname

dastan = University('Dastan')
dastan.add_department('sdfsdfsdf')
dastan.add_student('sdfsdfsdf', "ulik")

ulik = Student('Ulukbek', 'Kuvanychbekov')
dastan.add_student('sdfsdfsdf', ulik)