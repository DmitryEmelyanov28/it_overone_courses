# # class car:
# #     def __str__(self):
# #         return 'car class object'
# #
# #     def start(self):
# #         print('двигатель заведен')
# #
# #
# # car = car()
# # print(car)
#
#
# # class Phone:
# #     def __init__(self, color, model):
# #         self.color = color
# #         self.model = model
# #
# #     def check_sim(self, mobile_operator):
# #         if self.model == 'pixel' and mobile_operator == 'MTS':
# #             print('ваш оператор мтс')
# #
# #     @staticmethod
# #     def model_hash(model):
# #         if model == 'pixel':
# #             print(model)
# #
# #     @classmethod
# #     def toy_phone(cls,color):
# #         toy_phone = cls(color,'Toy phone')
# #         return toy_phone
# #
# #
# #
# # my_phone = Phone('red', 'pixel')
# # my_phone.check_sim('MTS')
# # Phone.model_hash('pixel')
# # my_phone.model_hash('pixel')
# #
# # print(Phone.toy_phone('Red').color,Phone.toy_phone('Red').model)
# #
# # Создайте класс Human.
# # Определите для него два статических поля: default_name и default_age.
# # Создайте метод init(), который помимо self принимает еще два параметра: name и age.
# # Для этих параметров задайте значения по умолчанию, используя свойства default_name и default_age.
# # В методе init() определите четыре свойства: Публичные - name и age. Приватные - money и house.
# # Реализуйте справочный метод info(), который будет выводить поля name, age, house и money.
# # Реализуйте справочный статический метод default_info(), который будет выводить статические поля default_name и default_age.
# # Реализуйте метод earn_money(), увеличивающий значение свойства money.
# # class Human:
# #     default_name = 'Dima'
# #     default_age = '19'
# #
# #     def __init__(self, name=default_name, age=default_age):
# #         self.name = name
# #         self.age = age
# #         self.__money = 0
# #         self.__house = None
# #
# #     def info(self):
# #         print(self.name)
# #         print(self.age)
# #         print(self.__house)
# #         print(self.__money)
# #
# #     @staticmethod
# #     def default_info():
# #         print(Human.default_age, Human.default_name)
# #
# #     def earn_money(self, x):
# #         self.__money += x
# #         print('было добавлено ', x, 'денег', 'всего денег :', self.__money)
# #
# #
# # Human.default_info()
# # human_obj = Human(input('введите имя: '), input('введите возраст :'))
# # human_obj.info()
# # human_obj.earn_money(int(input('введите количество денег :')))
# # human_obj.info()
#
#
# # родительский класс
# # class Phone:
# #     # иниацилизатор
# #     def __init__(self):
# #         self.is_on = False
# #
# #     # включаем телефон
# #     def turn_on(self):
# #         self.is_on = True
# #
# #     # если телефон включен делаем звонок
# #     def call(self):
# #         if self.is_on:
# #             print('Making call...')
# #
# #     # унаследованный класс
# #
# #
# # class Mobilephone(Phone):
# #     # добавляем новое свойство battery
# #     def __init__(self):
# #         super().__init__()
# #         self.battery = 0
# #
# #     # заряжая телефон на величину переданного значения
# #     def charge(self, num):
# #         self.battery = num
# #         print(f'charging battery up to ...{self.battery}%')
# #
# #
# # my_mobile_phone = Mobilephone()
# # print(dir(my_mobile_phone))
#
#
# # создаем класс Vehicle
# # class Vehicle:
# #     def vehicle_method(self):
# #         print("Это родительский метод из класса Vehicle")
# #
# # # создаем класс Car, который наследует Vehicle
# # class Car(Vehicle):
# #     def car_method(self):
# #         print("Это дочерний метод из класса Car")
# # # создаем класс Cycle, который наследует Vehicle
# # class Cycle(Vehicle):
# #     def cycleMethod(self):
# #         print("Это дочерний метод из класса Cycle")
# # car_a = Car()
# # car_a.vehicle_method()  # вызов метода родительского класса
# # car_b = Cycle()
# # car_b.vehicle_method()  # вызов метода родительского класса
#
#
# # class Camera:
# #     def camera_method(self):
# #         print('это родительский метод из класса Camera')
# #     def info(self):
# #         print('info1')
# #
# #
# # class Radio:
# #     def radio_method(self):
# #         print('родительский метод из класса Radio')
# #
# #     def info(self):
# #         print('info2')
# #
# #
# # class Callphone(Camera, Radio):
# #     def call_phone_method(self):
# #         print('это дочерний метод из класса CallPhone')
# #
# #
# # call_phone_a = Callphone()
# # call_phone_a.camera_method()
# # call_phone_a.radio_method()
# # call_phone_a.info() #если у методов одинаковые названия то вызовется о
# # н только один раз для класса который записан в скобах первым
#
# # Класс House
# # 1. Создайте класс House
# # 2. Создайте метод init() и определите внутри него два динамических свойства: _area
# # и _price. 3. Свои начальные значения они получают из параметров метода init()
# # 4. Создайте метод final_price(), который принимает в качестве параметра размер скидки
# # и возвращает цену с учетом данной скидки.
# #
# # Класс SmallHouse
# # 1. Создайте класс SmallHouse, унаследовав его функционал от класса House
# # 2. Внутри класса SmallHouse переопределите метод init() так, чтобы он создавал объект с площадью 40м2
# #
# # Класс Human
# #  1. Реализуйте приватный метод make_deal(), который будет отвечать за техническую реализацию
# #  покупки дома: уменьшать количество денег на счету и присваивать ссылку на только что купленный дом.
# #  В качестве аргументов данный метод принимает объект дома и его цену.
# # 2.  Реализуйте метод buy_house(), который будет проверять, что у человека достаточно денег д
# # ля покупки, и совершать сделку. Если денег слишком мало - нужно вывести предупреждение в консоль.
# # Параметры метода: ссылка на дом и размер скидки
# # class Human:
# #     default_name = 'Dima'
# #     default_age = '19'
# #
# #     def __init__(self, name=default_name, age=default_age):
# #         self.name = name
# #         self.age = age
# #         self.__money = 0
# #         self.__house = None
# #
# #     def info(self):
# #         print(self.name)
# #         print(self.age)
# #         print(self.__house)
# #         print(self.__money)
# #
# #     @staticmethod
# #     def default_info():
# #         print(Human.default_age, Human.default_name)
# #
# #     def earn_money(self, x):
# #         self.__money += x
# #         print('было добавлено ', x, 'денег', 'всего денег :', self.__money)
# #
# #     def __make_deal(self, house, price):
# #         self.__money -= price
# #         self.__house = house
# #
# #     def buy_house(self, house, discount):
# #         price = house.final_price(discount)
# #         if self.__money >= price:
# #             self.__make_deal(house, price)
# #             print('вы приобрели дом !')
# #         else:
# #             print('у вас нет денег!')
# #
# #
# # class House:
# #     def __init__(self, area, price):
# #         self._area = area
# #         self._price = price
# #
# #     def final_price(self, discount):
# #         final_price = self._price * (100 - discount) / 10
# #         print('финальная цена со скидкой :', final_price)
# #         return final_price
# #
# #
# # class Small_house(House):
# #     def _init__(self, price):
# #         super().__init__(40, price)
# #
# #
# # house1 = Small_house(500)
# # Human.default_info()
# # human_obj = Human(input('введите имя: '), input('введите возраст :'))
# # human_obj.info()
# # human_obj.earn_money(50)
# # human_obj.info()
# # human_obj.buy_house(house1, 10)
# # human_obj.info()
# # class Human:
# #     def_name = 'Glep'
# #     def_age = '21'
# #
# #     def __init__(self, name=def_name, age=def_age):
# #         self.name = name
# #         self.age = age
# #         self.__money = 0
# #         self.__house = None
# #
# #     def info(self):
# #         print(self.name, self.age, self.__money, self.__house)
# #
# #     @staticmethod
# #     def default_info():
# #         print(Human.def_age, Human.def_name)
# #
# #     def earn_money(self, x):
# #         self.__money += x
# #         print(self.__money)
# #
# #     def __make_deal(self, house, price):
# #         self.__money -= price
# #         self.__house = house
# #
# #     def buy_house(self, house, discount):
# #         price = house.final_price(discount)
# #         if self.__money >= price:
# #             self.__make_deal(house, price)
# #             print('Вы приобрели дом')
# #         else:
# #             print('У вас нет денег!')
#
#
# # Класс House
# # 1. Создайте класс House
# # 2. Создайте метод __init__() и определите внутри него два динамических свойства: _area и _price.
# # 3. Свои начальные значения они получают из параметров метода __init__()
# # 4. Создайте метод final_price(), который принимает в качестве параметра размер скидки и
# # возвращает цену с учетом данной скидки.
# # class House:
# #     def __init__(self, area, price):
# #         self._area = area
# #         self._price = price
# #
# #     def final_price(self, discount):
# #         final_price = self._price * (100 - discount) / 100
# #         print('Финальная цена со скидкой', final_price)
# #         return final_price
#
#
# # Класс SmallHouse
# # 1. Создайте класс SmallHouse, унаследовав его функционал от класса House
# # 2. Внутри класса SmallHouse переопределите метод __init__() так, чтобы он создавал объект с площадью 40м2
# # class SmallHouse(House):
# #     def __init__(self, price):
# #         super().__init__(40, price)
# #
# #
# # house1 = SmallHouse(500)
# #
# # Human.default_info()
# # Human1 = Human('Sasha', '13')
# # Human1.info()
# # Human1.earn_money(500)
# # Human1.buy_house(house1, 10)
# # Human1.info()
#
#
# class Phone:
#
#     def __init__(self):
#         self.is_on = False
#
#     def turn_on(self):
#         pass
#
#     def call(self):
#         pass
#
#     # Метод, который выводит короткую сводку по классу Phone
#     def info(self):
#         print(f'Class name: {Phone.__name__}')
#         print(f'If phone is ON: {self.is_on}')
#
#
# # Унаследованный класс
# class MobilePhone(Phone):
#
#     def __init__(self):
#         super().__init__()
#         self.battery = 0
#
#     # Такой же метод, который выводит короткую сводку по классу MobilePhone
#     # Обратите внимание, что названия у методов совпадают - оба метода называются info()
#     # Однако их содержимое различается
#     def info(self):
#         print(f'Class name: {MobilePhone.__name__}')
#         print(f'If mobile phone is ON: {self.is_on}')
#         print(f'Battery level: {self.battery}')
#
#
# def show():
#     for i in [Phone, MobilePhone]:
#         print(20 * '_')
#         obj = i()
#         obj.info()
#
#
# show()


class tEST:
    test = None

print(tEST.test)