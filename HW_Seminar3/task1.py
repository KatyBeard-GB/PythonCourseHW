# Задача 16: Требуется вычислить, сколько раз встречается 
# некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное 
# число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. 
# Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     3
#     -> 1

n = int(input('Сколько чисел вы хотите ввести? '))
array = list()
for i in range(n):
    array.append(int(input('Введите число массива: ')))
x = int(input('Какое проверить число? '))
result = 0
for i in array:
    if x == i: result += 1
print(f'Число {x} встречается {result} раз')