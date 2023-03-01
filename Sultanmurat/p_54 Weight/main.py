import math

class Weight:
    def __init__(self, centner, gram=0, kilogram=0):
        self.gram = int(gram)
        self.kilogram = int(kilogram)
        self.centner = int(centner)

    def __str__(self):
        return f'Вес {self.centner} центнеров, {self.kilogram} килограм и {self.gram} грам.'

    def weight_count(self):
        count = 0
        if self.centner != 0:
            count += math.floor(self.centner * 100000.25)
        if self.kilogram != 0:
            count += self.kilogram * 1000
        count += self.gram
        return count

    def __add__(self, other):
        return self.weight_count() + other.weight_count()

    def __sub__(self, other):
        return self.weight_count() - other.weight_count()

    def __gt__(self, other):
        return self.weight_count() > other.weight_count()
 
    def __it__(self, other):
        return self.weight_count() < other.weight_count()
        
    def __eq__(self, other):
        return self.weight_count() == other.weight_count()
        
    def __ne__(self, other):
        return self.weight_count() != other.weight_count()
        
    def __ge__(self, other):
        return self.weight_count() >= other.weight_count()
        
    def __le__(self, other):
        return self.weight_count() <= other.weight_count()