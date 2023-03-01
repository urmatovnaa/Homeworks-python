class Employee:
    def __init__(self, name, lastname, salary):
        self.name = name
        self.lastname = lastname
        self.salary = salary

    def give_raise(self, salary_plus=5000):
        self.salary += salary_plus