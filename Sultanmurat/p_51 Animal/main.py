class Animal:
    def eat(self):
        print('Animal is eating')
    
    def sleep(self):
        print('Animal is sleeping')

    def make_sound(self):
        print('Animal is making sound')

class AnimalWithHorn:
    def gorn(self):
        print('The animal butts horns')

class Cow(Animal, AnimalWithHorn):
    pass

class Ram(Animal, AnimalWithHorn):
    pass

cow = Cow()
ram = Ram()

cow.eat()
cow.sleep()
cow.make_sound()

ram.eat()
ram.sleep()
ram.make_sound()

cow.gorn()
ram.gorn()