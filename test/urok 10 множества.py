# num_set = {15, 6, 4, 2}
# print(num_set)
# a = {'Python',[1,2,3], 'c++', 'c'}
# print(a)
# a = [1, 2, 2, 'asd', 4, 5]
# print(a)
# a_2 = set(a)
# print(a_2)
# a_3 = {2,213,2,45,6,7,'asd'}
# print(a_3,len(a_3))
# d = {}
# print(type(d))
# b = set()
# print(type(b))
# months = {'jan', 'feb', 'march', 'aprl', 'may', 'june', 'july', 'august', 'sept', 'oct', 'nov', 'dec'}
# # for i in months:
# #     print(i)
# # print('may'in months)
# months.add('anton')
# months.add('may')
# print(months)
# num_set = {1, 2, 3, 4, 5, 6}
# num_set.discard(3)
# print(num_set)
# num_set.remove(3) #будет выдовать ошибку если элемента в множестве не существует
# print(num_set)
# x = num_set.pop()
# print(x)
# num_set.clear()
# print(num_set)
# months_a = {'jan','feb','march','apr','may','june'}
# months_b = {'july','august','sept','oct','nov','dec'}
# all_months = months_a.union(months_b)
# print(all_months)
# x = {1, 2, 3}
# y = {4, 3, 6}
# z = {7, 4, 9}
# output = x.union(y, z)
# print(output)
# months_a = {'jan', 'feb', 'march', 'apr', 'may', 'june'}
# months_b = {'july', 'august', 'sept', 'oct', 'nov', 'dec'}
# print(months_a | months_b) #обьединение
# x = {1, 2, 3}
# y = {3, 4, 5}
# print(x & y)
# a = {1, 2, 3}#разница между множествами,элементы которые содержатся в одном множестве но не содержатся в другом
# b = {4, 3, 6}
# print(a - b)
# print(b - a)
names_a = {'dima', 'anton', 'nikitos'}
names_b = {'jeffry', 'anton', 'andrew'}
x = names_a.isdisjoint(names_b)  # метод проверяет пересечения между множествами,если нет пересечений то выводит true
print(x)
# my_set = frozenset([1, 2, 3, 4, -10, 40])#неизменяемое множество
# print(type(my_set))
import random

# a = [1, 1, 2, 3, 4, 5]
# b = set(a)
# if len(a) > len(b):
#     print('есть дубликать')
# else:
#     print('нет дубликатов')
# a = {1, 2, 3, 4, 5}
# b = frozenset([5, 6, 7, 8, 9])
# print(a | b)
# # print(a & b)
# a = 'python ,JS! C?'
# b = set()
# for i in a:
#     if not i.isalpha() and i != '':
#         a = a.replace(i, ' ')
# b = set(a.split())
# print(b)
# print(a)