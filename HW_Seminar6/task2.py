# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

import random as r

array = []
for i in range(10): array.append(r.randint(-100,100))
print(array)
minDiapazon, maxDiapazon = [int(i) for i in input('Введите диапазон через пробел: ').split()] 
print('Индексы элементов массива:', end=' ')
for ind_number in range(len(array)):
    if array[ind_number] >= minDiapazon and array[ind_number] <= maxDiapazon:
        print(f'{ind_number}({array[ind_number]})', end=' ')