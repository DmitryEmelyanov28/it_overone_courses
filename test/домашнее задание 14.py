# Если в функцию передаётся кортеж, то посчитать длину всех его слов.
# Если список, то посчитать кол-во букв и чисел в нём.
# Число – кол-во нечётных цифр.
# Строка – кол-во букв.
# Сделать проверку со всеми этими случаями.
def funct(a):
    count = 0
    bukv = ''
    num = []
    if type(a) is tuple:
        for i in a:
            if i != ' ':
                count += 1
        print('длина всех слов кортежа :', count)
    elif type(a) is list:
        for i in a:
            if type(i) is int:
                # print(i)
                num.append(i)
            elif type(i) is str:
                # print(i)
                bukv += i
        print('количество букв :', len(bukv), 'количество цифр :', len(num))
    elif type(a) is int:
        for i in str(a):
            if int(i) % 2 != 0:
                count += 1
        print('количество нечетных чисел :', count)
    elif type(a) is str:
        for i in a:
            if i.isalpha():
                count += 1
        print('количество букв :', count)


funct(tuple('Hello dmitry'))
funct([1, 2, 3, 4, 'wasd', 'qwerty'])
funct(13579)
funct('Hello my name is Dmitry!')
