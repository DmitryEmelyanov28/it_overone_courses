# import random
#
# n = random.randint(1, 10)
# print('случайное число', n)
# n_2 = random.randint(100, 999)
# print(n_2)
# a = int(input('a = :'))
# b = int(input('b = :'))
# n_3 = random.randint(a, b)
# print('случайное число', n_3)
# 1 sposob
# a = int(input('Введите число a :'))
# b = float(input('Введите число b :'))
# c = input('Введите строку :')
# d = bool(input('введите :'))
# a_1 = str(a)
# b_1 = str(b)
# d_1 = str(d)
# print(a_1)
# print(b_1)
# print(c)
# print(d_1)
# #2 spsob
# a = str (a)
# print (a, type(a))
# b = str (b)
# print (b, type (b))
# a = 5
# b = 5
# #1 sposob
# c = a == b
# print(c)
# #2 sposob
# print (a==b)
# a = 10
# if a == 10:
#     print('a =10')
# else:
#     print('а не равно 10')
# print('ya ne blok')
# a = int(input('Введите число a :'))
# if a % 2==0:
#     print('число четное')
# else:
#     print('число не четное')a
# a = int(input('введите число a :'))
# if a == 10:
#     print('a = 10')
# elif a == 7:
#     print('a = 7')
# elif a == 5:
#     print('a = 5')
# else:
#     print('ничего не подошло')
# a = 'hello'
#
# if a == 'hello':
#     print('равно')
# else:
#     print('не равно')
# a = int(input('Введите порядковый номер пальца руки :'))
# if a == 1:
#     print('большой палец')
# elif a == 2:
#     print('указательный палец')
# elif a == 3:
#     print('средний палец')
# elif a == 4:
#     print('безымянный палец')
# elif a == 5:
#     print('мизинец')
# else:
#     print('неверный номер пальца')
# a = int(input('a ='))
# b = int(input('b ='))
#
# if a == 10 and b == 10:
#     print('a= 10 и b=10')
# elif a == 7 or b == 7:
#     print('a=7 или b=7')
# elif a == 1 and b == 1 or c == 77:
#     print('a=1 и b=1 или c =7')
# else:
#     print('ничего не подошло')
# print(not True)
a = int(input('введите a :'))
b = int(input('введите b :'))
c = int(input('введите c :'))
if a>b and a>c:
    print('число a - наибольшее')
elif b>a and b>c:
    print('число b - наибольшее ')
elif a==b and a==c:
    print('все числа равны')
else:
    print('число c - наибольшее')