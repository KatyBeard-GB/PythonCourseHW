# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), 
# не превосходящие числа N.

N = int(input('Введите число: '))
answer = 0
s = ''
while 2**answer < N:
    s += str(2**answer)
    s += ' '
    answer += 1
print(s)