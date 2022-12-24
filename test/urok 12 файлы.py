# f = open('1.txt', 'r', encoding='utf-8')
# # f2 = open('С:/1.txt', 'r', encoding='utf-8') #указываем путь
# print(f)
# print(*f)
# f.close() #закрываем файл
# f = open('1.txt', 'r', encoding='utf-8')
# try:
#     print(*f)
# finally:
#     f.close()
# with open('1.txt', 'r', encoding='utf-8') as f: #автоматически закрывает файл
#     print(*f)
# print('я не отношусь к with')
# with open('1.txt', 'r', encoding='utf-8') as f:
#     s = (f.read())
# print(s, type(s))
# with open('1.txt', 'r', encoding='utf-8') as f:
#     # s = f.readline()
#     # s2 = f.readline()
#     s = f.readlines()
# print(s,type(s))
# s_new = []
# for i in s:
#     i = i.replace('\n','')
#     s_new.append(i)
# print(s_new)
# f = open('2.txt','w')
# f.write('Hello! \nWorld')
# f.close()
# import os

# os.rename('1.txt','first.txt')
# print('текущая директория :',os.getcwd())
# os.mkdir('folder')
# print('текущая директория :',os.getcwd())
# os.chdir('folder')
# print('текущая директория :',os.getcwd())
# f = open('2.txt','w')
# f.write('abnana')
# f.close()
# print('текущая директория :',os.getcwd())
# os.chdir('folder')
# print('текущая директория :',os.getcwd())
# os.chdir('..')
# print('текущая директория :',os.getcwd())
# os.makedirs('n1/n2/n3')
# os.remove('folder/2.txt')
# # os.rmdir('folder')
# os.removedirs('n1/n2/n3')
with open('', 'r', encoding='utf-8') as f:
    s = f.readlines()
c = []
for i in s:
    i = i.replace('_', '')
    if i.isdigit():
        c.append(i)
print(c)
import os
# with open('second.txt','w') as f:
#     while True:
#         s = input('enter str ')
#         if s == '':
#             break
#         f.write(s + '\n')
