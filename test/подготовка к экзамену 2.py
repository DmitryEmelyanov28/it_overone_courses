# # ана строка, состоящая ровно из двух слов, разделенных пробелом.
# # Переставьте эти слова местами. Результат запишите в строку и
# # выведите получившуюся строку.
# # Замените в этой строке все цифры 1 на слово one
# # Примечание: решить без использования функции split
#
#
# # a = input('Введите строку состоящую из 2-х слов')
# # print(a)
# # b = str
# # ind = (a.find(' '))
# # c = a[::ind]
# # b = [ind:]
# #
# # # print(ind)
# # a = 'one 1'
# # v = []
# # n = ''
# # for i in a:
# #     if i.isalpha() or i.isdigit():
# #         n += i
# #     else:
# #         if n != '':
# #             v.append(n)
# #             n = ''
# # if n != '':
# #     v.append(n)
# # print(a)
# # v2 = v[1] + ' ' + v[0]
# # print(v2)
# # v2 = v2.replace('1', 'one')
# # print(v2)
# #
# # a = 'one 1'
# # a1 = a.index(' ')
# # a2 = a[:a1]
# # a3 = a[a1 + 1:]
# # a4 = a2 + ' ' + a3
# # a4 = a4.replace('1', 'one')
# # print(a4
# # for i in range(1, 10):
# #     for a in range(1, 10):
# #         print(i * a, end='\t')
# #     print()
# # Сгенерировать список из 10 чисел. Диапазон чисел - 0, 9.
# # Посчитайте, сколько в нем пар элементов, равных друг другу.
# # Любые два элемента, равные друг другу образуют одну пару,
# # которую необходимо посчитать. При этом образованная пара не участвуют в формировании других пар.
# # Вывести цифру из списка '-' количество пар с этой цифрой.
# # Например, [1, 1, 1, 1].
# # 1 - 2
# # Результат: 2 пары.
# import random
#
# my_list = [random.randint(0, 9) for i in range(10)]
# cn = 0
# print(my_list)
# for i in set(my_list):
#     print(i, my_list.count(i)//2)
#     cn +=my_list.count(i)//2
# print('Пар в списке :',cn)
# for i in range(1, 10):
#     for a in range(1, 10):
#         print(i * a,  end='\t' )
#     print()
# Даны два кортежа:
# A = (13, 5, 43, 49, 67, 32)
# B = (53, 21, 4, 23)
# Необходимо определить:
# 1) Сумма элементов какого из кортежей больше и вывести соответствующее сообщение на экран ( Сумма больше в кортеже - ..)
# 2) Вывести на экран порядковые номера минимальных элементов этих
# кортежей
# A = (13, 5, 43, 49, 67, 32)
# B = (53, 21, 4, 23)
# sum_a = sum(A)
# sum_b = sum(B)
# print('Сумма A:', sum_a)
# print('Сумма B:', sum_b)
# if sum_a > sum_b:
#     print('сумма A больше')
# else:
#     print('Сумма B больше')
# a = A.index(min(A))
# b = B.index(min(B))
# print('порядковый номер минимального элемента A :', a + 1)
# print('порядковый номер минимального элемента B :', b + 1)
# list1 = [1, 2, 3]
# list2 = ['abc', 'asd', 'zxc']
# a = dict(zip(list1, list2))
# print(a)
# import random
#
# a = [random.randint(0, 9) for i in range(5)]
# b = [random.randint(0, 9) for x in range(5)]
# list1 = a + b
# print(a)
# print(b)
#
# a_1 = set(a)
# b_1 = set(b)
# d = a_1 | b_1
# c = 0
# for i in d:
#     c = a_1 & b_1
#     m = len(list(c))
# print(c)
# print('количество повторяющихся элементов :', m)


# Сгенерировать n множеств (нумерацию начать с 1).
# Вывести элементы, которые входят во все множества с номерами,
# кратными трём, но не входят в первое множество.
# import random
# n = 10
# m_all = set()
# for i in range(1, n+1):
#     m = {random.randint(1, 10) for i in range(10)}
#     if i == 1:
#         m1 = m.copy()
#     if i%3 == 0:
#         print('кратное 3 ',i,m)
#         for i_2 in m:
#             if i_2 not in m1:
#                 m_all.add(i_2)
#  print(m1)
#  print(m_all)
class Test:
    __test = 0


print(Test.__test)
