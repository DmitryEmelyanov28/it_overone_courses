# 1.Сформулируйте SQL запрос для создания таблицы movies.
# Поля: movie_id, name TEXT, release_year INTEGER, genre TEXT 2.
# Создать функции:1. Добавить фильм (заполнение делать с клавиатуры)
# 2. Получения данных обо всех фильмах      3. Получения данных об одном фильме по id
# 0. Выход3. Функции вызывать в цикле, чтоб у пользователя был выбор.
import sqlite3

movies = sqlite3.connect('movies.db')
cursor = movies.cursor()
cursor.execute(
    '''CREATE TABLE IF NOT EXISTS tab_1 (movie_id INTEGER PRIMARY KEY AUTOINCREMENT, 
    name TEXT, release_year INTEGER,genre TEXT) ''')


def add_film():
    name = input('Введите название фильма :')
    release_year = int(input('Введите год выпуска фильма :'))
    genre = input('Введите жанр фильма :')
    cursor.execute('''INSERT INTO tab_1(name,release_year,genre) VALUES (?,?,?)''', (name, release_year, genre))
    movies.commit()
    cursor.execute('''SELECT * FROM tab_1''')


def films_info():
    k = cursor.fetchall()
    print(k)


def film():
    movie_id = int(input('Введите id фильма :'))
    b = """select * from tab_1 where movie_id = ?"""
    cursor.execute(b, (movie_id,))
    records = cursor.fetchall()
    for row in records:
        print("ID:", row[0])
        print("Название фильма:", row[1])
        print("Год выпуска", row[2])
        print("Жанр", row[3])


for i in cursor.fetchall():
    print(i)
while True:
    choice = input('''
    1 - добавить фильм
    2 - Данные обо всех фильмах
    3 - данные о фильме по id
    0 - выход из программы 
    Выберите функцию:''')
    if choice == '1':
        add_film()
    if choice == '2':
        films_info()

    if choice == '3':
        film()
    if choice == '0':
        print('Вы вышли из программы')
        break
