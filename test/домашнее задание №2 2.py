# Человек вводит день и месяц своего рождения,
# выведите, кем он является по знаку зодиака
day = int(input('Введите день своего рождения :'))
month = int(input('Введите месяц своего рождения :'))
if month == 3 and day >= 21 and day <= 31 or month == 4 and day >= 1 and day <= 20:
    print('овен')
elif month == 4 and day >= 21 and day <= 31 or month == 5 and day >= 1 and day <= 21:
    print('телец')
elif month == 5 and day >= 22 and day <= 31 or month == 6 and day >= 1 and day <= 21:
    print('близнецы')
elif month == 6 and day >= 22 and day <= 31 or month == 7 and day >= 1 and day <= 22:
    print('рак')
elif month == 7 and day >= 23 and day <= 31 or month == 8 and day >= 1 and day <= 23:
    print('лев')
elif month == 8 and day >= 24 and day <= 31 or month == 9 and day >= 1 and day <= 22:
    print('дева')
elif month == 9 and day >= 23 and day <= 31 or month == 10 and day >= 1 and day <= 23:
    print('весы')
elif month == 10 and day >= 24 and day <= 31 or month == 11 and day >= 1 and day <= 22:
    print('скорпион')
elif month == 11 and day >= 23 and day <= 31 or month == 12 and day >= 1 and day <= 21:
    print('стрелец')
elif month == 12 and day >= 22 and day <= 31 or month == 1 and day >= 1 and day <= 20:
    print('козерог')
elif month == 1 and day >= 21 and day <= 31 or month == 2 and day >= 1 and day <= 18:
    print('водолей')
else:
    print('Рыбы')