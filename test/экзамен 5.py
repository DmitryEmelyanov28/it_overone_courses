# Посчитать, сколько пар (стоят рядом) верхнего и нижнего регистра находится в
# веденном с клавиатуры слове. (Пример HjkLM- 1 пара нижнего, 1 пара верхнего), а
# также сколько всего букв в слове, сколько гласных и согласных.
a = input('Введите слово :')
gls = 0
sgl = 0
b = ''
c = ''
para_verh = 0
para_niz = 0
vse_gls = "aeiuoyAEIUOY"
vse_sogl = "bcdfghjklmnpqrstvwxzBCDFGHJKLNMPQRSTVWXZ"
for i in a:
    if i.isupper():
        b += i
        if len(b) % 2 == 0:
            para_verh += 1
    # elif b != '':
    #     b = ''
    elif i.islower():
        c += i
        print(c)
        if len(c) % 2 == 0:
            para_niz += 1
    # elif c != '':
    #     c = ''
for i in a:
    if i in vse_gls:
        gls +=1
    elif i in vse_sogl:
        sgl += 1

print('Количество пар верхнего регистра :', para_verh)
print('Количество пар нижнего регистра :', para_niz)
print('Количество гласных :' , gls)
print('Количество согласных :' , sgl)
