# for i in range(10):
#     print('i =', i) #i=int
#     print('hello')
# for i in range(4,8): # от 4 до 8не включая 8
#     print('i =', i) #i=int
#
# for i in range(4,10,2): #4 до 10 не включая с шагом 2
#     print('i =', i) #i=int
#
# import random
#
# r = random.randint(1, 10)
# for i in range(4):
#     n = int(input('n = '))
#     if n == r:
#         print('win')
#     else:
#         print('Lose')
# print(r)
#

# s = 'Hello,Я учу Python!'
# s_2 = ''
# for i in s:
#     if i.isupper():
#         print(i, end=' ')
#         # s_2 = ''
#         # s_2 = '' + 'H'
#         # s_2 = 'H' + 'P'
#         # s_2 = 'HЯ' + 'P'
#         s_2 = s_2 + i  # s_2 +=i
# print()
# print(s_2)
# for i in range(15, 0, -1):
#     print( i ,end=' ')
# s = input('Введите строку: ')
# s_2 = input('Введите символ: ')
# s_new = ''

# for i in s:
#     if i != s_2:
#         # print(i)
#         s_new += i
# print(s_new)

# #Вводится начало,конец и шаг последовательности,нужно вывести на экран данную последовательность чисел
# a = int(input('Введите начало последовательности :'))
# b = int(input('Введите конец последовательности :'))
# c = int(input('Введите шаг последовательности :'))
# d = int
# for i in range(a, b, c):
#     print('Последовательность :', i)
#
# a = []  # пустой список
# b = ['hello', 'world', 'python']
# n = [1, 45, 123, 76, 24]
# for i in n:
#     print(i)
#     if i == 123:
#         break
# print('я не отношусь к циклу')
# n = [1, 45, 123, 76, 24]
# for i in n:
#     if i == 123:
#         continue
#     print(i)
#
# print('я не отношусь к циклу')
# n = [1, 45, 123, 76, 24]
# n.append(77777)
# a_ch = []
# for i in n:
#     if i %2 == 0:
#     #print(i)
#         a_ch.append(i)
# print(a_ch)
# n = []
# for i in range(54, 9184):
#     if i % 5 == 0:
#         n.append(i)
# print(n)
# a = [2, 4, 5, 10]
# s = 0
# pr = 1
# for i in a:
#     #print[i]
#     print(pr)
#     pr *= i
#     s +=i
# print('Сумма: ', s)
# print('Произведение: ', s)
# a = [2, 4, 6, 7, 8, 2, 5, 3, 2]
# print(a.count(4))
