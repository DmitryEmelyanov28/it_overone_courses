# Казино. Компьютер генерирует числа от
# 1 до 10 и от 1 до 2-х соответственно. Цифры от одного до 10
# отвечают за номера, а от 1 до 2 за цвета(1-красный,2 черный).
# Пользователю дается 5 попыток угадать номер и цвет
# (Прим. введения с клавиатуры: 3 красный).
# В случае неудачи вывести на экран правильную комбинацию.
import random
i = 1
win_number = random.randint(0, 10)
win_colour = random.randint(1, 2)
while i < 6:
    number = int(input('Выберете число от 1 до 10 :'))
    colour = int(input('Выберете цвет,1 - красный, 2 - черный :'))
    if number == win_number and colour == win_colour:
        print('Вы победили!')
    else:
        print('Вы проиграли!')
    i += 1
    if win_colour == 1:
        print('Выигрышный цвет: красный')
    elif win_colour == 2:
        print('Выигрышный цвет: черный')
    print('Победила цифра : ', win_number)


