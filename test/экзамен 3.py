# Посчитать, сколько раз встречается определенная цифра в числах. Количество
# введенных чисел и искомая цифра задаются с клавиатуры. Числа выбираются
# рандомно.
import random
# a = int(input('Введите число :'))
n = int(input('Выберете количество чисел в списке :'))
a = [random.randint(0, 100) for i in range(n)]
print(a)
c = int(input('Введите цифру,которую хотите посчитать в a: '))
stroka = str(a)
c_1 = str(c)
d = stroka.count(c_1)
print('Количество цифр : ', d)



