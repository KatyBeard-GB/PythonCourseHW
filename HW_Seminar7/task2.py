# Задача 36: Напишите функцию 
# def print_operation_table(operation, num_rows=6, num_columns=6), 
# которая принимает в качестве аргумента функцию, 
# вычисляющую элемент по номеру строки и столбца. 
# Аргументы num_rows и num_columns указывают число строк 
# и столбцов таблицы, которые должны быть распечатаны. 
# Нумерация строк и столбцов идет с единицы 
# (подумайте, почему не с нуля). 
# Примечание: бинарной операцией называется любая операция, 
# у которой ровно два аргумента, как, например, у операции умножения.

# *Пример:*

# **Ввод:** `print_operation_table(lambda x, y: x * y) ` 
# **Вывод:**
# 1 2 3 4 5 6

# 2 4 6 8 10 12
# 3 6 9 12 15 18
# 4 8 12 16 20 24
# 5 10 15 20 25 30
# 6 12 18 24 30 36

def print_operation_table(operation, num_rows=6, num_columns=6):
    for row in range(1, num_rows + 1):
        for column in range(1, num_columns + 1):
            print(operation(row, column), end=' ')
        print()

operators = list(filter(lambda x: x != 'print_operation_table', input('Введите функцию: ').split('(')))
operators = list(filter(lambda x: x != ')', operators[0]))
countComma = len(list(filter(lambda x: x == ',', operators)))

temp_rows = 0
temp_columns = 0
operator = ''
rows = ''
columns = ''

for i in operators:
    if i == ',' and countComma == 3:
        temp_columns = 1
        operator += i
        countComma -= 1
    elif i == ',' and countComma == 2 and temp_columns == 0: 
        temp_rows = 1
        operator += i
        countComma -= 1
    elif i == ',' and (temp_rows == 1 or temp_columns == 1): 
        temp_rows, temp_columns = 2, 2
    elif i == ',' and temp_columns == 2: 
        temp_columns, temp_rows = 3, 3
    elif temp_rows == 2: rows += i
    elif temp_columns == 3: columns += i
    else: operator += i

if rows == '':
    print_operation_table(eval(operator))
elif columns == '':
    print_operation_table(eval(operator), int(rows))
else:
    print_operation_table(eval(operator), int(rows), int(columns))