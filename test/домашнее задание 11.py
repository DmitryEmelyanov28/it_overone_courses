# Файл содержит числа и буквы. Каждый записан в отдельной строке.
# Нужно считать содержимое в список так, чтобы сначала шли числа по возрастанию,
# а потом слова по возрастанию их длинны.
new_list = []
new_list_2 = []
with open('dz.txt', 'r', encoding='utf-8') as f:
    a = f.read()
    # print(a)
    my_list = a.split()
    for i in my_list:
        if i.isdigit():
            new_list.append(int(i))
        else:
            new_list_2.append(i)
new_list.sort()
new_list_2.sort(key=len)
print(new_list + new_list_2)





# for i in a:
#     if i.isdigit():
#         # i = i.split()
#         new_list.append(i.split())

# my_list.sort(key=len)
# print(my_list)
# for i in a:
#     print(i)
# # for i in a:
# # if i.isdigit():
# my_list.append(a)
# my_list.sort()
# for i in my_list:
#     i = i.replace('\n', '')
# print(my_list)
