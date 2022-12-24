# У вас есть словарь, где ключ – название продукта. Значение – список, который содержит цену и кол-во товара.
# Выведите через ‘’–’’ название – цену – количество.
# С клавиатуры вводите название товара и его кол-во. n – выход из программы.
# Посчитать цену выбранных товаров и сколько товаров осталось в изначальном списке.
fruits = {'Apple': [3, 10],
          'Banana': [5, 6]}
for key, values in fruits.items():
    print(key, '-', values[0], 'p', '-', values[1], 'кг')
print('''Введите фрукт который вы хотите купить:
      Apple - яблоко
      Banana - банан
      n - выход из программы''')
price = 0
last_weight1 = []
a = ''
for i in fruits:
    choice = input('Введите фрукт которых хотите выбрать :')
    if choice == 'n':
        exit()
    else:
        weight = int(input('Введите количество товара :'))
        price += weight * fruits[choice][0]
        last_weight = fruits[choice][1] - weight
        last_weight1.append(last_weight)
        print('остаток товара', choice, last_weight, 'кг')
print('цена выбранных товаров составляет :', price, 'p')
