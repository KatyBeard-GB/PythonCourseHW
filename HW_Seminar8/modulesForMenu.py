from tabulate import tabulate
from menuHW import *

def AddData():
    file = open('contacts.txt', 'r', encoding='UTF-16')
    count = 1
    for line in file:
        count = len(list(filter(lambda el: el == ';', line))) + 1
    file.close()
    file = open('contacts.txt', 'a', encoding='UTF-16')
    first_name = input('\nВведите имя: ')
    second_name = input('Введите фамилию: ')
    mid_name = input('Введите отчество: ')
    number = input('Введите номер телефона: ')
    item = [str(count), first_name, second_name, mid_name, number]
    file.writelines('.'.join(item))
    file.writelines(';')
    file.close()

def PrintData():
    file = open('contacts.txt', 'r', encoding='UTF-16')
    print()
    for line in file:
        item = line.split(';')
        data = []
        for i in item:
            if i != '':
                data.append(i.split('.'))
        head = ['ID', 'Имя - 1', 'Фамилия - 2', 'Отчество - 3', 'Номер телефона - 4']
        print(tabulate(data, headers=head, tablefmt="grid"))
        input("Нажмите Enter для продолжения...")
        MenuHW()
    file.close()

def SearchData():
    file = open('contacts.txt', 'r', encoding='UTF-16')
    strSearch = input('\nВведите информацию для поиска контакта (имя, фамилию, отчество, номер телефона): ').lower()
    for line in file:
        item = line.split(';')
        data = []
        for i in item:
            if i != '' and strSearch in i.lower():
                data.append(i.split('.'))
        if data == []:
            if int(input('\nТакой информации в справочнике нет. Вывести все контакты? (Да - 0, Нет - 1) ')) == 0:
                PrintData()
            else: break
        else:
            print('\nНайденные контакты:\n')
            head = ['ID', 'Имя', 'Фамилия', 'Отчество', 'Номер телефона']
            print(tabulate(data, headers=head, tablefmt="grid"))
            input("Нажмите Enter для продолжения...")
    file.close()