# В текстовом файле посчитать количество строк,
# а также для каждой отдельной строки определить количество в ней символов.
with open('dz12.txt', 'r+') as f:
    s = f.readlines()
s_new = []
for i in s:
    i = i.replace('\n', '')
    i = i.replace(' ', '')
    s_new.append(i)
print(s_new)
print('Количество строк в списке :', len(s_new))
for i in s_new:
    print('Количество символов в', (s_new.index(i) + 1), 'строке :', len(s_new[s_new.index(i)]))
