from modulesForMenu import *

def Menu():
    flag = True
    while flag:
        print('\n1 --> Добавить контакт \n2 --> Вывести все контакты \n3 --> Поиск по контактам \n4 --> Выход')
        num = int(input('\nВыберите пункт меню: '))
        if num == 1: AddData()
        if num == 2: PrintData()
        if num == 3: SearchData()
        if num == 4: flag = False