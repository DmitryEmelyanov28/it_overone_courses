# def a_function():
#     '''
#     функция просто печатает текст!
#     '''
#     print('You just created a function!')
# a_function()
# def empty_function():
#     """
#     пустая функция
#     """
#     pass  # позволяет делать пустыые функции
#
#
# empty_function()
# import random
#
#
# def suma():
#     a = [random.randint(0, 10) for i in range(5)]
#     print(a)
#     return sum(a)
#
#
# print(suma())
# arr = [1, 2, 3, 4]
#
#
# def a():
#     r = 0
#     for i in arr:
#         r += i
#     # # print(r)
#     return r
# print(a())
# f_obj = a()
# print(f_obj,type(f_obj))
# def add(a, b):
#     return a + b
#
#
# print(add(1, 2))
# print(add(3, 4))
# def add(a,b):
#     print('a:',a,"b:",b)
#     return a + b
#
#
# print(add(1, 2))
# print(add(3, 4))
# print(add(b=12,a = 2))
# def mix(a, b=12, c=2):
#     print(a, b, c)
#     return a + b + c
#
#
# print(mix(2))
# print(mix(1, b=2, c=3))
# def many(*args, **kwargs):
#     print(args)
#     for i in args:
#         print(i)
#     for key, value in kwargs.items():
#         print(key, '-', value)
#
#
# many(1, 2, 'arg', 3, name='anton', surname='ivanov')
# def f_a():
#     global a
#     a = 1
#     b = 2
#     return a + b
#
#
# print(f_a())
#
#
# def f_b():
#     c = 4
#     return a + c
#
#
# print(f_b())

# def f(a, b):
#     def fun_2(x):
#         return x * x * x
#
#     return fun_2(a) + fun_2(b)
#
#
# print(f(4, 5))
# def s(a, b): return a + b
#
#
# print(s(1, 2))
# def is_year_leap(year):
#     if (year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
#         return True
#     else:
#         return False
#
# print(is_year_leap(1700))
# def season(n):
#     if n > 2 and n < 6:
#         return 'весна'
#     elif n > 5 and n < 9:
#         return 'лето'
#     elif n > 8 and n < 12:
#         return 'осень'
#     else:
#         return 'зима'
#
#
# print(season(int(input())))
# import math
#
#
# def square(a):
#     return 4 * a, a * a, math.sqrt(2) * a
#
#
# print(square(int(input('Введите сторону квадрата :'))))
# def abc(a, b):
#
#     return a/b
#
#
#
#
#
# print(abc(int(input()), int(input())))
##рекурсия
# def factorial(n):
#     if n != 0:
#         return n * factorial(n - 1)
#     else:
#         return 1
#
#
# print(factorial(5))
# def funct(x): return x
#
#
# a1 = funct
# a2 = a1
# print(a2(10))
# def s(a, b): return a + b
#
#
# print(s(1, 2))
# s_2 = lambda x, y: x + y
# print(s_2(2, 3))
# print((lambda x, y: x + y)(1, 2))
# s_2 = lambda x = 1, y = 2: x + y
# power = s_2
# print(s_2())
# print(power(3))
# def f_1(a):
#     def f_2(b):
#         return a * b
#
#     return f_2
#
#
# print(f_1(2)(3))  # a =  2,b =3
# three_f = f_1(3) #a = 3
# print(three_f(10))
# def f_1():
#     print('first test')
#
#
# def f_2():
#     print('second test')
#
#
# def simple_decore(fn):
#     def wrapper():
#         print('start function')
#         fn()
#         print('stop function')
#
#     return wrapper
#
#
# first_f_1 = simple_decore(f_1)
# first_f_1()
# second_f_2 = simple_decore(f_2)
# second_f_2()
# def simple_decore(fn):
#     def wrapper():
#         print('start function')
#         fn()
#         print('stop function')
#
#     return wrapper
#
# @simple_decore
# def f_1():
#     print('first test')
#
# @simple_decore
# def f_2():
#     print('second test')
#
# f_1()
# f_2()
# def decore(fn):
#     def wrapper(arg):
#         print('strt function', str(fn.__name__), 'with param:', arg)
#         fn(arg)
#
#     return wrapper
#
#
# @decore
# def print_sqrt(num):
#     print(num ** 0.5)
#
#
# print_sqrt(4) # num = arg = 4

# def razr(a):
#     count = 0
#
#     while a != 0:
#         a //= 10
#         count += 1
#     return count
#
#
# print('количество разрядов :',razr(int(input('введите число a:'))))
#
#
# def razr_1(b):
#     return len(str(b))
#
#
# print('количество разрядов :',razr_1(int(input('введите число b:'))))
#
# def funct(*args, **kwargs):
#     my_list = []
#     for i in args:
#         if args.index(i) % 2 != 0:
#             my_list.append(i)
#     for x in kwargs.values():
#         if type(x) is str:
#             my_list.append(x)
#
#     return my_list
#
#
# print(funct(1, 2, 3, 4, 5, a='hi', b='12', c='name'))

# import random
#
#
# def funct(a, b):
#     print([random.randint(a, b) for i in range(10)])
#
#
# funct(int(input('Введите начало диапазона :')), int(input('Введите конец диапазона :')))

def count(a):
    vse_gl = 'aeyuoiAEYUOI'
    vse_sogl = 'BCDFGHJKLMNPQRSTVWXZbcdfghjklmnpqrstvwxz '
    count_glas = 0
    count_sgl = 0
    for i in a:
        if i != ' ':
            if i in vse_gl:
                count_glas += 1
            elif i in vse_sogl:
                count_sgl += 1

    print('количество гласных :', count_glas)
    print('количество согласных :', count_sgl)


count(input('Введите строку :'))
