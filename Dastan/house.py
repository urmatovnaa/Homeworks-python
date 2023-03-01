# 1.	Создайте класс House a. Создайте метод __init__()
# и определите внутри него два динамических атрибута:
# material (тип материала из которого построен дом) и address (месторасположение дома).
# Свои начальные значения они получают из параметров метода __init__()
# По умолчанию material = brick (кирпич)

class House:
    def __init__(self, adress, material='brick'):
        self.adress = adress
        self.material = material
        self.area = 78


# 2.	Определите внутри класса статический атрибут area (площадь) и укажите значение 78.
# 3.	Используя нижеописанные таблицы создайте метод get_price()
# которая будет выдавать цену за квадратный метр Материал
# Материал	Цена за кв. метр
# brick (кирпич)	350
# sand_block (пескоблок)	250
# marble (мрамор)	500
# other (какой то другой материал)	300

    def get_price(self):
        global adress_price, material_price
        material = {'brick':350, 'sand_block':250, 'marble':500, 'other':300}
        adress = {'town':1.3, 'outskirts':1.1, 'village':0.7}
        for k, v in material.items():
            if self.material == k:
                material_price = v
        for k, v in adress.items():
            if self.adress == k:
                adress_price = v
        return material_price * adress_price



# Месторасположение дома	Цена за кв. метр
# town (город)	Цена * 1.3
# outskirts (окраина города)	Цена * 1.1
# village (деревня)	Цена * 0.7
#
#
# 4.	То есть если дом находится в деревне и сделан из кирпича, то:
# Цена за квадратный метр = 350 * 0.7 = 245
# 5.	Создайте метод full_price(), который рассчитывает общую стоимость дома,
# то есть area * get_price() (Цена за квадратный метр)

    def full_price(self, area):
        return area * self.get_price

# 6.	Создайте метод final_price, который принимает в себя такой параметр как condition
# (состояние дома) и используя таблицу ниже выдавайте итоговую стоимость
# Состояние дома	Цена
# bad	Цена * 0.8
# good	Цена * 1
# excellent	Цена * 1.2
    def final_price(self, condition):
        if condition == 'bad':
            return full_price * 0.8
        elif condition == 'good':
            return full_price * 1
        elif condition == 'excellent':
            return full_price * 1.2

# 7.	Создайте статический метод show_house, который принимает в себя в
# качестве аргумента состояние погоды и в зависимости от погоды будет выдавать следующее
    @staticmethod
    def show_house(pogoda):
        if pogoda == 'rainy':
            print('Сегодня идет дождь, к сожалению посмотреть дом не получится')
        elif pogoda == 'shiny':
            print('Сегодня отличная погода, чтобы съездить и посмотреть дом Вашей мечты')
        elif pogoda == 'snowy':
            print('Сегодня снежная погода, оденьтесь потеплее')
        else:
            print("Такой погоды нет")
# Погода	Ответ
# rainy	Сегодня идет дождь, к сожалению посмотреть дом не получится
# shiny	Сегодня отличная погода, чтобы съездить и посмотреть дом Вашей мечты
# snowy	Сегодня снежная погода, оденьтесь потеплее
#
    @classmethod
    def create_house(cls, dict_1):
        return cls(dict_1['adress'], dict_1['мaterial'])

# 8.	Создайте класс-метод create_house который будет принимать в себя словарь и на
# основе словаря будет создавать экземпляр класса.
# Пример словаря = { ‘мaterial’ : ‘brick’, ‘address’ : town }
#
# 9.	Создайте стандартный обычный метод get_info, который будет выдавать привлекательное описание дома.
# 10.	 Создайте класс Apartment который будет наследоваться от класса House

class Apartment(House):
    def __init__(self,adress, material, floor):
        self.floor = floor
        super().__init__(adress, material)


    def get_price_1(self, floor):
        if 1 <= floor <= 5:
            self.get_price() * 1.1
        else:
            self.get_price() * 0.9






# a. Добавьте ему динамическое поле (атрибут) floor (этаж на котором находится квартира) b.
# Перепишите метод get_price() добавьте дополнительно проверку на этажи, если квартира находится
# от 1 этажа до 5 этажа, то цена = цена * 1.1, если квартира находится от 5 этажа до 9 этажа включительно,
# то цена = цена * 0.9
house1 = House('town', 'other')
print(house1.get_price())