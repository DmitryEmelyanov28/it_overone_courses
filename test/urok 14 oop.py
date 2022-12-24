# class Car:
#     defoult_color = 'Grey'  # обычное свойство класса
#
#     # динамические свойства класса
#     def __init__(self, color, model):
#         self.color = color
#         self.model = model
#
#     def turn_on(self):
#         # print('Включаем!')
#         return 'Включаем!'
#
#     def ride(self):
#         pass
#
#     def info(self):
#         print('Статическое свойство default_color', self.defoult_color,'динамическое свойство color model',self.color,
#               self.model)
#
#
# car_obj = Car('red', 'tesla')
# car_obj2 = Car('black', 'bmw')
# car_obj.info()
# car_obj2.info()
# car_obj2 = Car()
# print(dir(car_obj))
# print(car_obj.defoult_color)
# print(car_obj.color, car_obj.model)
# print(car_obj2.color, car_obj2.model)
# print(car_obj.defoult_color)
# print(car_obj2.turn_on())
# class Car:
#     def __init__(self, color, type, year):
#         self.color = color
#         self.type = type
#         self.year = year
#
#     def turn_on(self):
#         return 'Автомобиль заведен'
#
#     def turn_off(self):
#         return 'Автомобиль заглушен'
#
#     def god(self):
#         return self.year
#
#     def tip(self):
#         return self.type
#
#     def cvet(self):
#         return self.color
#
#
# car_obj = Car(input('Введите цвет:'), input('введите тип :'), input('введите год выпуска :'))
# print(car_obj.turn_on())
# print(car_obj.turn_off())
# print(car_obj.god())
# print(car_obj.tip())
# print(car_obj.cvet())


class Example:
    a = 2
    b = 3

    def __init__(self, a1, b1):
        self.a1 = a1
        self.b1 = b1

    def f1(self):
        c = 5
        print('переменная созданная внутри функции :', c)

    def f2(self):
        print('сумма статичных пееременных :', self.a + self.b)

    def f3(self):
        print('возвдение числа a в степень b1', self.a1 ** self.b1)

    def info(self):
        print('Статическое свойство :', self.a)


a_obj = Example(int(input('введите число a1 :')), int(input('введите число b1 ')))
a_obj.f1()
a_obj.f2()
a_obj.f3()
a_obj.info()
