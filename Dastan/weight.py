import math

# Создайте класс Weight (Вес).
class Weight:

# kilogram (килограммы, целочисленное значение) и centner (центнер, целочисленное значение) .
# Свои начальные значения они получают из параметров метода __init__ ().
# Если не указывать значения gram и kilogram, то по умолчанию их значение равна 0.
    def __init__(self, centner, gram=0, kilogram=0):
        self.centner = centner
        self.gram = gram
        self.kilogram = kilogram

# Напишите магический метод __str__ () в котором будет возвращаться информация: «Вес .. центнеров, .. кг, .. гр».
    def __str__(self):
        return f'Вес {self.centner} центнеров, {self.kilogram} кг, {self.gram} гр'

    def gramms(self):
        cntnr = 100000 * self.centner
        kg = 1000 * self.kilogram
        sum = kg + cntnr + self.gram
        return sum

# Напишите методы прибавления __add__ и убавления __sub__ для данного класса
    def __add__(self, other):
        return self.gramms() + other.gramms()

    def __sub__(self, other):
        return self.gramms() - other.gramms()

# Напишите методы сравнения двух экземпляров класса (__eq__, __gt__, __le__ и т.д.)
    def __gt__(self, other):
        return self.gramms() > other.gramms()

    def __lt__(self, other):
        return self.gramms() < other.gramms()

    def __eq__(self, other):
        return self.gramms() == other.gramms()

    def __ne__(self, other):
        return self.gramms() != other.gramms()

    def __ge__(self, other):
        return self.gramms() >= other.gramms()

    def __le__(self, other):
        return self.gramms() <= other.gramms()
# Создайте отдельный файл для проверки класса Weight. В данном файле проверьте:
# Результат прибавления одного экземпляра класса на другой
# Результат убавления одного экземпляра класса от другой
# И все сравнения двух экземпляров класса (__eq__, __gt__, __le__ и т.д.)

a = Weight(10, 200, 15)
b = Weight(15, 30, 50)
print(a + b)
print(a - b)
print(a > b)
print(a < b)
print(a == b)
print(a != b)
print(a >= b)
print(a <= b)





