# print("100 200 300 400".count("0"))
# print("100 200 300 400".count("0", 3, 7))
# print("100 200 300 400".count("0", 3))
# stroka = input('Введите текст :')
# gls = 0
# sogl = 0
# vse_gls = "aeiuoy"
# vse_sogl = "bcdfghjklmnpqrstvwxz"
# for i in stroka:
#     if i in vse_gls:
#         gls += 1
#     elif i in vse_sogl:
#         sogl += 1
# print('Количество гласных :', gls)
# print('Количество согласных :', sogl)
# a = int(input('Введите число a :'))
# b = int(input('Введите число b :'))
# c = int(input('Введите число c :'))
# list = [a, b, c]
# if a > b and a < c:
#     print('число a - среднее :', a)
# elif b > a and b < c:
#     print('число b - среднее :', b)
# elif c > a and c < b:
#     print('число c - среднее :', c)
# list.sort()
# print('среднее число :', list[1])
# Список из 7 цифр. Если четных цифр в нем больше чем нечетных,
# то найти сумму всех его цифр, если нечетных больше,
# то найти произведение 1 3 и 6 элемента.
# list = [5, 2, 3, 4, 5, 6, 7]
# ch = 0
# nech = 0
# for i in list:
#     if type(i) is int and i % 2 == 0:
#         ch += 1
#     else:
#         nech += 1
# print('количество четных',ch)
# print('количество нечетных',nech)
# if ch > nech:
#     print('сумма : ', sum(list))
# else:
#     pr = list[0] * list[2] * list[5]
# #     print('произведение :', pr)
# a = int(input('Введите число '))
# list = [a]
# b = len(list)
# i = 0
# print(list)
# a = (input("Введите число:"))
# b = a[::-1]
# c = int(b)
# print('перевернутое число :' ,c)
# import random
#
# a = [random.randint(1, 5) for i in range(10)]
# suma = 0
# pr = 1
# for i in a:
#     suma = sum(a)
#     pr *= i
# print('исходный список :', a)
# print('сумма :', suma)
# print('произведение :', pr)
# a = 'hello world hello'
# b = a.split()
# print(b)
# b_2 = ','.join(b)
# print(b_2)
# Введите слово c клавиатуры, которое состоит из букв разных регистров. Нужно посчитать
# кол-во пар верхнего регистра.
# Парой считаются две рядом стоящие буквы верхнего регистра.
# Например, HeLLoO – одна пара LL.
# a = input('Введите слово :')
# r = ''
# p = 0
# for i in a:
#     if i.isupper():
#         r += i
#         print(r)
#         if len(r) % 2 == 0:
#             p += 1
#     elif r != '':
#         r = ''
# print('Количество пар ', p)
# a = [4, 6, 'pу', 'tell', 78]
# b = [44, 'hello', 56, 'exept', 3]
# c = a + b
# c.insert(3, c[5])
# print('исходный список ',c)
# for i in c:
#     if type(i) is str:
#         c.remove(i)
# print('длина списка :', len(c))
# print('поменяли местами ', c)
list = [13, 10, 15, 3, 12]
x =list.sort()
print(list)