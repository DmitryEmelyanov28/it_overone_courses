# Дан список list=[15,48,'hello',6,19,'world’].
# Все числа этого списка проверить на чётность.
# Если число чётное, то посчитать сумму его цифр. Если нечётное, то заменить  его на 1 в списке.
# Все слова: посчитать количество гласных и согласных.
# Вывести всё на экран.
my_list = [15, 48, 'hello', 6, 19, 'world']
# b = []
# c = []
n = len(my_list)
print(type(my_list[-1]))
summ_ch = 0
vse_gl = 'aeyuoi'
gl = 0
sogl = 0
for i in my_list:
    gl = my_list.count('e')
    if type(i) == int and i % 2 == 0:
        print('число четное : ', i)
        digit = i % 10
        if digit != 0:
            summ_ch += digit
        i = i // 10
    elif type(i) == int and i % 2 != 0:
        ind = my_list.index(i)
        my_list[ind] = 1
        print('число не четное', i)
    # if type(i) == str:
    #     print('Это слова : ', i)
    #     gl = my_list.count(vse_gl)
    # else:
    #     sogl += 1
    if i == 'o' or i == 'e':
        gl += 1

print('Сумма цифр четных чисел :', summ_ch)
print('Отредоктированный список : ', my_list)
print('Количество гласных букв :', gl)
print('Количество согласных букв :', sogl)

# glas = 'aeyuoi'
# sogl = 'qzwsxdcrvtgbhnjmklp'
# b = []
# c = []
# for i in my_list:
#     if i in vse_gl:
#         b.append(i)
# print('гласных :',len(b))
# # for e in my_list:
# #     if e in sogl:
# #         c.append(e)
# # print('Согласных :',len(c))
