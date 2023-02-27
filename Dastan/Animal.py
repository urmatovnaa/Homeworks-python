# Создайте классы Animal и AnimalWithHorn.
# В первом должны быть методы eat, sleep, make_sound. Во втором должен быть метод gore (бодать рогами).
# Создайте субклассы Cow и Ram которые должны наследоваться от двух классов Animal и AnimalWithHorn.
# Создайте экземпляры Cow, Ram, вызовите методы с обеих родительских классов.

class Animal:
    def eat(self):
        print("Eat")

    def sleep(self):
        print("Sleep")

    def make_sound(self):
        print("make_sound")


class AnimalWithHorn:

    def gore(self):
        print("I'm goring now !!!")

class Cow(Animal, AnimalWithHorn):
    pass


class Ram(Animal, AnimalWithHorn):
    pass

burenka = Cow
print(burenka.eat)
print(burenka.make_sound)
print(burenka.sleep)

diablo = Ram
print(diablo.gore)