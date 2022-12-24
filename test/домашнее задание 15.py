# Калькулятор.
# Создайте класс, где реализованы функции(методы) математических операций. А также функция, для ввод данных.
class calc:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        return self.a + self.b

    def subtraction(self):
        return self.a - self.b

    def mult(self):
        return self.a * self.b

    def division(self):
        try:
            self.a / self.b
        except ZeroDivisionError:
            return 'деление на ноль!'
        return self.a / self.b


calc_obj = calc(int(input('Введите число a :')), int(input('Введите число b :')))
while True:
    choice = input("""
     + - сложение
    - вычитаение
    / - деление
    * - умножение
    0 - выход из программы
    выберите операцию :""")
    if choice == '+':
        print('сумма :', calc_obj.addition())
    elif choice == '-':
        print('разность :', calc_obj.subtraction())
    elif choice == '*':
        print('произведение :', calc_obj.mult())
    elif choice == '/':
        print('частное :', calc_obj.division())
    elif choice == '0':
        print('вы вышли из программы!')
        exit()
