def ReadFile():
    file = open('contacts.txt', 'r', encoding='UTF-16')
    dFile = []
    for line in file:
        item = line.split(';')
        for i in item:
            if i != '':
                dFile.append(i.split('.'))
    file.close()
    return dFile

def ResultEnd(dataR, id, head, dataItem):
    result = []
    resultItem = []
    for item in dataR:
        if item[0] == id:
            for i in range(len(item)):
                if i == head:
                    resultItem.append(dataItem)
                else: resultItem.append(item[i])
            result.append('.'.join(resultItem))
        else: result.append('.'.join(item))
    return result

def ChangeData():
    idChange = input('\nВведите ID контакта, который Вы хотите изменить: ')
    headChange = int(input('\nЧто Вы хотите изменить? (Имя - 1, Фамилия - 2, Отчество - 3, Номер телефона - 4) '))
    dataChange = input('\nВведите измененные данные: ')
    dataC = ReadFile()
    file = open('contacts.txt', 'w', encoding='UTF-16')
    result = ResultEnd(dataC, idChange, headChange, dataChange)
    file.writelines(';'.join(result) + ';')
    file.close()

def DeleteData():
    idDelete = input('\nВведите ID контакта, который Вы хотите удалить: ')
    dataD = ReadFile()
    file = open('contacts.txt', 'w', encoding='UTF-16')
    result = []
    if int(input('Вы хотите полностью его удалить? (Да - 0, Нет - 1) ')) == 0:
        for item in dataD:
            if item[0] != idDelete:
                result.append('.'.join(item))
    else:
        headDelete = int(input('\nКакие данные Вы хотите удалить? (Имя - 1, Фамилия - 2, Отчество - 3, Номер телефона - 4) '))
        result = ResultEnd(dataD, idDelete, headDelete, '')
    file.writelines(';'.join(result) + ';')
    file.close()
    