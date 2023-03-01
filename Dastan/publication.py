# Реализуйте родительский класс Publication, конструктор которого принимает name, date, pages, library, type

class Publication:
    def __init__(self, name, date, pages, library, type_1):
        self.name = name
        self.date = date
        self.pages = pages
        self.library = library
        self.type_1 = type_1

        # В классе Publication создайте метод get_code_in_library()
        # который будет возвращать первые_2_буквы_библиотеки_тип_первые_2_буквы_названия_количество_страниц_дата_без_точек

    def get_code_in_library(self):
        return f' Библиотека : {self.library[0:2]}, тип :{self.type_1}, название :{self.name[0:2]}, ' \
               f'количество страниц :{self.pages}, дата : {self.date.split(".")}'

# Создайте субкласс Book. В конструктор родительского класса должен передавать type=’book’

class Book(Publication):
    def __init__(self, name, date, pages, library, type_1='book'):
        super().__init__(name, date, pages, library, type_1)

# Создайте субкласс Magazine. В конструктор родительского класса должен передавать type=’magazine’

class Magazine(Publication):
    def __init__(self, name, date, pages, library, type_1='magazine'):
        super().__init__(name, date, pages, library, type_1)

# Создайте субкласс Newspaper. В конструктор родительского класса должен передавать type=’newspaper’

class Newspaper(Publication):
    def __init__(self, name, date, pages, library, type_1='newspaper'):
        super().__init__(name, date, pages, library, type_1)



hobbit = Book('Hobbit', '13.06.2002', 580, 'Bishkek')
print(hobbit.get_code_in_library())

goal = Magazine('Goal', '15.06.2022', 50, "Bishkek")
print(goal.get_code_in_library())
