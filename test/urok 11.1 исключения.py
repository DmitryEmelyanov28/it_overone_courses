# my_dict = {'a': 1, 'b': 2, 'c': 3}
# try:
#     my_dict['123']
# except KeyError as e:
#     print('не существует ключа')
#
#     print(e)
# print('result :', my_dict)
# list = [1, 2, 3, 4]
# try:
#     list[8]
# except IndexError as e:
#     print('не существует indexa')
# my_dict = {'a': 1, 'b': 2, 'c': 3}
# try:
#     my_dict[1]
# except KeyError as e:
#     print('такого ключа нет')
# except IndexError as e:
#     print('не существует индекса')
# except:
#     print('произошла ошибка')
# my_dict = {'a': 1, 'b': 2, 'c': 3}
# try:
#     my_dict['a']
# except (KeyError, IndexError):
#     print('произошло исключение error or indexerror')
# else:
#     print('ошибок нет')
# finally:
# #     print('оператор finally был вызван')
# a = int(input('введите число a:'))
# b = int(input('введите число b:'))
# try:
#     a / b
# except ZeroDivisionError:
#     print('деление на 0')
#     result = 0
# else:
#     print('возведение в квадрат',(a / b)**2)
# finally:
#     print('оператор finally вызван')

try:
    a = int(input('введите число a:'))
    b = int(input('введите число b:'))
    a / b
except ZeroDivisionError:
    print('деление на 0')
    result = 0
except ValueError:
    print('Введены не целые числа')
except Exception as e:
    print(e)
else:
    print('результат =', (a / b))
finally:
    print('оператор finally вызван')
