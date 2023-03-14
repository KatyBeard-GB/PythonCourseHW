from modulesHW import *

def MenuHW():
    flag = True
    while flag:
        print('\n1 --> Изменить данные справочника \n2 --> Удалить данные из справочника \n3 --> Выйти в главное меню')
        num = int(input('\nВыберите пункт меню: '))
        if num == 1: ChangeData()
        if num == 2: DeleteData()
        if num == 3: flag = False