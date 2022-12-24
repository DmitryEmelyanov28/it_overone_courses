# Посчитать, сколько раз встречается цифра 1 в списке чисел, заполненных рандомно.
# Диапазон случайного числа [1000, 9999]
# Кол-во чисел: 10
import random

list = [random.randint(1000, 9999) for i in range(10)]
count_1 = 0
a = 0
stroka = str(list)
for i in stroka:
    if i == '1':
        a += 1
print('Количество 1 в списке :', a)
print('Количество 1 в списке(2 способ) :', stroka.count("1"))
print(list)
