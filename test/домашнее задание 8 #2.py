# Преобразовать текст в кортеж слов с удалением знаков препинания.
a = input('введите текст :')
b = []

zn = '!.,?'
for i in a:
    if i not in zn:
        b.append(i)
c = (''.join(b))
d = tuple(str(i) for i in c.split(' '))
print(d)
print(type(d))
