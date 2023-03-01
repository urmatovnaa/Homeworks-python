# Создайте экземпляры, вызовите методы.
# Создайте экземпляры, вызовите все методы.

# Создайте класс Student. При создании его экземпляра,
# мы должны записать имя и фамилию студента в соответствующие переменные объекта.
class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        #  В классе должны быть:
        self.books = [] # переменная объекта books = [ ]
        self.knowledge = 0 # переменная объекта “knowledge” со значением по умолчанию 0
        self.languages = {} # В класс Student добавьте переменную экземпляра languages = { }
        self.is_ready_to_work = False # Добавьте в класс Student переменную объекта is_ready_to_work = False.

# метод read_book, который принимает название книги, добавляет книгу в books, добавляет 100 баллов в knowledge
    def read_book(self, book_name):
        self.book.append(book_name)
        self.knowledge += 100

# метод do_homework, который при вызове добавляет 10 баллов в knowledge
    def do_homework(self):
        self.knowledge += 10

# Добавьте метод learn_new_language, который принимает название языка программирования,
# и целочисленное от 1 до 100, добавляет в словарь languages язык в качестве ключа,
# баллы в качестве значения. Выкидывает ошибку ValueError, если балл меньше 1 и больше 100.
    def learn_new_language(self, name_of_language, mark):
        if mark < 1 or mark > 100:
            print("Value Error")
        else:
            self.languages[name_of_language] = mark

# Добавьте метод do_real_world_project, при вызове которого в knowledge добавляется 50 баллов.
    def do_real_word_project(self):
        self.knowledge += 50

# Добавьте метод add_points, который принимает баллы, добавляет в knowledge.
# Добавьте следующую проверку в метод add_points: если значение knowledge больше 2000,
# то выводим текст “This student is ready to work” и записывает True в is_ready_to_work.
    def add_points(self, marks):
        self.knowledge += marks
        if self.knowledge > 2000:
            self.is_ready_to_work = True
            print("This student is ready to work")
