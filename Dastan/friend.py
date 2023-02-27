# Создайте класс, сохраняющий каждый экземпляр в переменную класса all_contacts = [ ].
# В инициализаторе класса должны быть параметры name, lastname, phone_number. Подсказка: подумайте о self.
# Создайте субкласс Friend, у которого должен быть метод play_football_with_me()
# Создайте класс ContactList, который должен наследоваться от встроенного класса list.
# В нем должен быть реализован метод search_by_name, который должен принимать имя, и возвращать список всех совпадений.
# Замените all_contacts = [ ] на all_contacts = ContactList(). Создайте несколько контактов, используйте метод search_by_name.



class ContactList(list):

    def search_by_name(self, name):
        name_list = []
        for i in self:
            if name == i.name:
                name_list.append(i)
        return name_list


class Person:
    all_contacts = ContactList()

    def __init__(self, name, lastname, phone_number):
        self.name = name
        self.lastname = lastname
        self.phone_number = phone_number
        self.all_contacts.append(self)


osmon = Person('altynai', 'ghth', 67666)

class Friend(Person):
    def play_football_with_me(self):
        pass




