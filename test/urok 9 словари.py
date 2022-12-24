# d = {}
# d = {'dict':1,'dictionary':2}
# print(d)
# d = dict(short='dict', long='dictionary')
# d_2 = dict([(1, 1), (2, 4)])
# print(d, '\n', d_2)
# d = dict.fromkeys(['a', 'b'])
# d_2 = dict.fromkeys(['a', 'b'], 100)
# print(d, '\n', d_2)
# import random
#
# d = {i: i ** 2 for i in range(7)}
# print(d)
# d2 = {i: random.randint(1, 10) for i in range(7)}
# print(d2)
# d3 = {i: random.randint(1,10) for i in ['a', 12, 'bs', 7]}
# print(d3)
# d = {1: 'python', 2: 'java', 3: 'hello'}
# d[3] = 'c++'
# d[4] = 'js'
# print(d, d[2])
# print(len(d))
# Операция del - удаление элемента из словаря

# Исходный словарь
# Salary = {'Director': 120800.0,
#           'Secretary': 101150.25,
#           'Locksmith': 188200.00}
#
# print(Salary)
# # Удалить элемент по ключу 'Secretary'
# del Salary['None']
# print(Salary)

# Попытка удалить несуществующий ключ
# del Salary[5] - так нельзя, генерируется исключение KeyError: 5
# del Salary['None'] - тоже запрещено
# d = {'Name':['Diana','Joe','Justin'],
#      'Phone':['pixel','samsung'],
#      'dict':{'lang': 'Python',1 : 'hello'}}
# c1 = len(d['Name'])
# print(c1)
# print(d['dict']['lang'])
# if 'Phone' in d:
#     print('yes')
#
# # 1 сформировать пустой словарь
# Words = dict()  # Words = {}
#
# # # 2 ввести количество слов в словаре
# count = int(input("Количество слов в словаре"))
#
# # #3 цикл добавления слов
# i = 0
# while i <count:
#     print("Ввод слов")
#     wrd = input("слово :")
#     value = int(input('значение: '))
#
#     #если ключа wrd нет в словаре,то добавить пару [wrd:value]
#     if wrd not in Words:
#         Words[wrd] = value
#     i += 1
# print(Words)
# словари функция zip()
# создание словаря   из списков ключей и значений
# Numbers = dict(zip([1, 2, 3], ['one', 'two', 'three']))
# print(Numbers)
# исходный словарь
Months = {1: 'Jan', 2: 'Feb', 3: 'Mar',
          4: 'Apr', 5: 'May', 6: 'Jun',
          7: 'Jul', 8: 'Aug', 9: 'Sep',
          10: 'Oct', 11: 'Nov', 12: 'Dec'}
# print(Months.keys())
# print(Months.values())
# print(Months.items())
# F
for key, values in Months.items():
    print(key, ':', values)
# person = {'name': 'Dima',
#           'age': 18,
#           'city': 'Grodno'}
# print('Возраст :', person['age'])
# d = {'BMW': ['x2', 'x3', 'x4'],
#      'Tesla': ['model S', 'model X', 'model R']
#      }
# print(d['BMW'][0], d['BMW'][-1])
# print(d['Tesla'][0], d['Tesla'][-1])

# d1 = {"a": 100, "b": 200, "c": 300}
# d2 = {'a': 300, 'b': 200, 'd': 400}
# print(d1["b"]==d2["b"])
# d = {'a': 2, 'b': 3, 'c': 4}
# pr = 1
# for i in d:
#     pr *= d[i]
# print('произведение:', pr)
