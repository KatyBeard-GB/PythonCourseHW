# Задача 18: Требуется найти в массиве A[1..N] 
# самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число 
# N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. 
# Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5

n = int(input('Сколько чисел вы хотите ввести? '))
array = list()
for i in range(n):
    array.append(int(input('Введите число массива: ')))
x = int(input('Какое задать число? '))
count = 1000000
for i in array:
    if abs(x - i) < count: 
        count = x - i
        result = i
print(f'Самый близкий по величине элемент к заданному числу {x} -> {result}')