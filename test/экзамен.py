#  С клавиатуры вводится текст, определить,
#  сколько в нём гласных, а сколько
# согласных. В случае равенства
#  вывести на экран все гласные буквы.
a = input('Введите текст :')
gl = 0
sgl = 0
vse_gls = "aeiuoy"
vse_sogl = "bcdfghjklmnpqrstvwxz"
for i in a:
    if i in vse_gls:
        gl += 1
    elif i in vse_sogl:
        sgl += 1
for i in a:
    if gl == sgl:
        if i in vse_gls:
            print('Все гласные :', i)
print('Гласные :', gl)
print('Согласные :', sgl)
