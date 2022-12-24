# # # # # # letters = 'ЫгВЫоЯСремДШНККАыкЩЙФа'
# # # # # # for letter in letters:
# # # # # #     if letter.islower():
# # # # # #         print(letter, end='')
# # # # # #
# # # # # # letters = 'ЫгВЫоЯСремДШНККАыкЩЙФа'
# # # # # # letters_2 = ''
# # # # # # for letter in letters:
# # # # # #     if letter.islower():
# # # # # #         letters_2 += letter
# # # # # #
# # # # # # print(letters_2)
# # # # # while True:
# # # # #     print('Привет')
# # # # i = 0
# # # # while i < 20:
# # # #     print(i)
# # # #     i = i + 1
# # # #
# # # # for i_2 in range(10):
# # # #     print(i_2)
# # # i = 0
# # # while i < 20:
# # #     print(i)
# # #     if i == 5:
# # #         break
# # #     i = i + 1
# # i = 1
# # r = 0
# # while i < 51:
# #     print(i, end=' ')
# #     r += i
# #     i += 1
# # print()
# # print('Сумма :', r)
# #
# #
# # r_2 = 0
# # for i in range (51):
# #     r_2 +=i
# #     print(i, end = ' ')
# # print()
# # print('Сумма :', r_2)
# # Вывести на экран квадраты всех целых чисел от 1 до 10
# # i = 1
# # while i < 11:
# #     print(i ** 2, end=' ')
# #     i = i + 1
#
# # i = 1
# # s = 1
# # while  i < 125:
# #    if i % 2 == 0:
# #        s *= i
# #    i +=1
# #
# # print(s)
# #
# #
# # i = 0
# # while i < 10:
# #     print(i)
# #     if i == 55:
# #         break
# #     i = i + 1
# # else:  #else работает только в том случае если не был вызван break
# #     print('Готово')
# # for i in range(10):
# #     print(i)
# #     if i == 5:
# #         break
# # else:
# #     print('Готово')
# # i = 16
# # while i > 1:
# #     i += -1
# #     print(i)
# i = 0
# arr = []
# while i < 98:
#     i += +7
#     arr.append(i)
# print('Длина массива :', len(arr))
# print(arr)
# while True:
#     x = int(input('x ='))
#     y = int(input('x ='))
#     s = input('Знак + - * / 0 - выход : ')
#     if s == '0':
#         break
#     elif s == '+':
#         print(x + y)
#     elif s == '-':
#         print(x - y)
