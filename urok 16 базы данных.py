# import sqlite3
# import random
#
# conn = sqlite3.connect('name6.db')
# cursor = conn.cursor()
# cursor.execute(
#     '''CREATE TABLE IF NOT EXISTS tab_1 (id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 INTEGER, col_2 INTEGER) ''')
#
# for i in range(3):
#     x = random.randint(1, 9)
#     y = random.randint(1, 9)
#     cursor.execute('''INSERT INTO tab_1(col_1,col_2) VALUES (?,?)''', (x, y))
# conn.commit()
#
# cursor.execute('''SELECT col_1,col_2 FROM tab_1''')
# k = cursor.fetchall()
# print(k)
# s = 0
# for i in k:
#     for j in i:
#         s += j
# print('SUM', s)
# sr = (s / (len(k) * 2))
# print(sr)
#
# if sr > len(k):
#     cursor.execute('''DELETE FROM tab_1 WHERE id=4''')
# conn.commit()
# cursor.execute('''SELECT * FROM tab_1''')
# k = cursor.fetchall()
# print(k)
# import sqlite3
#
# # Создаём Базу данных
# conn = sqlite3.connect('name.sqlite3')
# # Создаем объект cursor, который позволяет нам взаимодействовать с базой данных и добавлять записи
# cursor = conn.cursor()
# # Создадим таблицу с двумя текстовыми колонками
# cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 TEXT,col_2 TEXT) ''')
#
# # Заполняем таблицу данными
# cursor.execute('''INSERT INTO tab_1(col_1,col_2) VALUES ('hello','world')''')
# # Сохраняем изменения
# conn.commit()
#
# d = "red"
# f = "black"
# cursor.execute('''INSERT INTO tab_1(col_1,col_2) VALUES (?,?)''', (d, f))
# conn.commit()
#
# cursor.execute('''SELECT*FROM tab_1''')
# k = cursor.fetchall()
# print(k)
#
# # Удаление записи из таблицы по id, по значению
# # cursor.execute('''DELETE FROM tab_1 WHERE id = 1''')
# # conn.commit()
# # cursor.execute('''DELETE FROM tab_1 WHERE col_1 ='red' ''')
# # conn.commit()
# cursor.execute('''SELECT*FROM tab_1''')
# k = cursor.fetchall()
# print(k)
# # обновление данных в таблице
# t = 3
# cursor.execute('''UPDATE tab_1 SET col_1 = 'world' WHERE id = ?''', (t,))
# conn.commit()
# cursor.execute('''SELECT*FROM tab_1''')
# k = cursor.fetchall()
# print(k)
# import sqlite3
# import random
#
# conn = sqlite3.connect('name1.db')
# cursor = conn.cursor()
# cursor.execute(
#     '''CREATE TABLE IF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 INTEGER,col_2 INTEGER) ''')
# # for i in range(3):
# #     x = random.randint(0, 9)
# #     y = random.randint(0, 9)
# #     cursor.execute('''INSERT INTO tab_1(col_1,col_2) VALUES (?,?)''', (x, y))
# conn.commit()
# cursor.execute('''SELECT col_1,col_2 FROM tab_1''')
# k = cursor.fetchall()
# print(k)
# cursor.execute('''SELECT id FROM tab_1''')
# k1 = cursor.fetchall()
# print(k1)
# r_id = random.choice(k1)
# print(r_id)
#
# cursor.execute('''SELECT col_1,col_2 FROM tab_1 WHERE id =?''', (r_id))
# r_1 = cursor.fetchall()
# print(r_1)
# print(r_1[0][0], r_1[0][1])
# if r_1[0][0] % 2 == 0 and r_1[0][1] % 2 == 0:
#     cursor.execute('''DELETE FROM tab_1 WHERE id = ?''', r_id)
#     print('произошло удаление')
# else:
#     cursor.execute('''UPDATE tab_1 SET col_1='world' WHERE id=?''', r_id)
#     print('произошло обновление')
#
# # conn.commit()
# cursor.execute('''SELECT * FROM tab_1''')
# k = cursor.fetchall()
# print(k)

# Создайте метод класса для работы с БД.
# Достаточно одной колонки в таблице. Тип INT.В БД:
# Если передан 1 аргумент, вставить в таблицу запись с числом
# 3.Если переданы 2 аргумента: проверить или второй аргумент
# является числом. Если условие верно, то удалить первую запись с БД.
# Если переданы 2 аргумента и их тип значений неизвестен, а 3 аргумент является числом,
# то обновить значение колонки БД на число 77 в 3 записи.
# import sqlite3
#
#
# conn = sqlite3.connect('name2.db')
# cursor = conn.cursor()
# cursor.execute(
#     '''CREATE TABLE IF NOT EXISTS tab_1 (id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 INTEGER) ''')
#
#
# # Если передан 1 аргумент, вставить в таблицу запись с числом 3.
# class A:
#     def method(self, a=None, b=None, c=None):
#         if a is not None and b is None and c is None:
#             print('INSERT')
#             cursor.execute('''INSERT INTO tab_1(col_1) VALUES (3)''')
#         # Если переданы 2 аргумента: проверить или второй аргумент является числом.
#         # Если условие верно, то удалить первую запись с БД.
#         elif a is not None and type(b) is int and c is None:
#             print('DELETE')
#             cursor.execute('''DELETE FROM tab_1 WHERE id=1''')
#         # Если переданы 2 аргумента и их тип значений неизвестен,
#         # а 3 аргумент является числом, то обновить значение колонки БД на число 77 в 3 записи.
#         elif a is not None and b is not None and type(c) is int:
#             print('UPDATE')
#             cursor.execute('''UPDATE tab_1 SET col_1=77 WHERE id=3''')
#
#
# a_obj = A()
# a_obj.method(234234, 'sdf',12)
#
# conn.commit()
# cursor.execute('''SELECT * FROM tab_1''')
# k = cursor.fetchall()
# print(k)

# import sqlite3
#
# conn = sqlite3.connect('name7.db')
# cursor = conn.cursor()
# cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1 (id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 TEXT, col_2 TEXT) ''')
# for i in range(3):
#     cursor.execute('''INSERT INTO tab_1(col_1,col_2) VALUES ('test','test2')''')
# cursor.execute('''DELETE FROM tab_1 WHERE id=2''')
# cursor.execute('''UPDATE tab_1 SET col_1 = 'hello', col_2 = 'world' WHERE id = 3 ''')
# cursor.execute('''SELECT * FROM tab_1''')
# k = cursor.fetchall()
# print(k)
#
# f = open('bd.txt', 'w')
# for i in k:
#     c = ','.join([str(x) for x in i])
#     print(c)
#     f.write(c + '\n')
# f.close()


# 1. Сформулируйте SQL запрос для создания таблицы book
# (book_id INT …, title TEXT, author TEXT, price INT, amount INT 2.
# Занесите новую строку в таблицу book с клавиатуры3. Выбрать информацию
# о всех книгах из таблицы book.
import sqlite3

book = sqlite3.connect('book.db')
cursor = book.cursor()
a = input('Enter title')
b = input('Enter author')
c = int(input('Enter price'))
d = int(input('Enter amount'))
cursor.execute(
    '''CREATE TABLE IF NOT EXISTS tab_1 (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, author TEXT,price INTEGER,amount INTEGER) ''')

# cursor.execute('''INSERT INTO tab_1(col_1,col_2) VALUES (?,?)''', (x, y))
cursor.execute('''INSERT INTO tab_1(title,author,price,amount) VALUES (?,?,?,?)''', (a, b, c, d))
book.commit()
cursor.execute('''SELECT * FROM tab_1''')
k = cursor.fetchall()
print(k)
