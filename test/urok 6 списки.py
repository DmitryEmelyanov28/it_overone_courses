# # elements = [1, 3, 'a',11]
# # print(elements)
# # # elements = list()
# # # print(elements)
# # a = [1, 3, 'a', 6, 'b']
# # print(a)
# # print(a[2], a[-1])
# # print(a[0:3], a[::2])
# import random
#
# a = [random.randint(0, 100) for i in range(10)]
# print(a, len(a))
# a = []
# a.append(123)
# print(a)
# a.insert(0, 'hi')  #в скобках первое число - это индекс,второе добавляемы элемент,добавляемый элемент сдвигает все индексы,но не заменяет их
# print(a)
# a.insert(2 , 'hello')
# print(a)
# a[-1] =7879
# print(a)
# ind = -1
# a[ind] = 1414141
# print(a)
# a = [1, 3, 'a', 6, 'b' ,'a']
# del a[0]  #удаление
# print(a)
# a.remove('a')
# a.remove('a')
# print(a)
# a = [1, 3, 'a', 6, 'b', 'a']
# del a[:5]  # удаление
# print(a)
# b = [1, 3, 'a', 6, [1, 2, 4, 5, 6, 1, 'a'], 51, 'afa']
# print(b[4][-1])
# b[4].append(55)
# print(b)
# a = [1, 3, 'a', 6, 'b', 'a']
# if 'a' in a:
#     print('Yes!')
# a = [1, 2, 3]
# b = [4, 5, 6]
# c = a + b
# print(a + b)
# print(c)
# a.extend(b)
# print(a)
# a = [23, 4, 57, 65, 234, 6]
# b = a
# print(a, b)
# a.append('hi')
# b.append(123456789)
# print(b, a)
# print(id(a), id(b))
# g = a.copy()
# g.append('hello')
# print(a, g)
# print(id(a), id(g))
# a = [12, 45, 312, 57, 8]
# for i in a:
#     print(i)
# a = [12, 45, 312, 57, 8]
# a_len = len(a)
# i = 0
# while i < a_len:
#     print(a[i])
#     i += 1

# # for i in a:
# #     print(i, '-', a.count(i))
# print(a.index(312))
# x = a.pop(2)
# print(x)
# print(a)
# a = [12, 45, 312, 57, 8, 2, 4, 45, 12]
# a.reverse()
# print(a)
# a.sort()
# print(a)
# a.sort(reverse=True)  #только если один тип данных в списке,по убыванию сортировка
# print(a)
# a = ['abc', 'a', 'bsadadsa', 'ab']
# a.sort(key=len)
# print(a)
# a.sort(key=len, reverse=True)
# print(a)
# a = [[1, 2, 3], ['abadbabdad', 'asd']]
# print(a[0][2])
# print(a[1][0])
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# a.reverse()
# print(a)
# print(a[::-1])
import random

# a = [20,111,1123131]
# if 20 in a:
#     ind= a.index(20)
#     a[ind]=200
# print(a)
# Список из 7 случайных чисел. Найти сколько четных и нечетных чисел. Добавить их в разные списки.
# import random
#
# a = [random.randint(0, 100) for i in range(7)]
# ch = []
# nech = []
# i = 0
# for i in a:
#     if i % 2 == 0:
#         ch.append(i)
#     else:
#         nech.append(i)
# print(a)
# print(ch)
# print(nech)
a = [1, 2, 3, 4, 5, 6, 7, 7, 8, 9, ]
print(a[::])
