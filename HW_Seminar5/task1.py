# Задача 26:  Напишите программу, которая на вход принимает 
# два числа A и B, и возводит число А в целую 
# степень B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

def Exponentiation(a, b, res = 1):
    if b == 0: return 1
    if b == 1: return a*res
    return Exponentiation(a, b-1, res*a)

num, degree = [int(i) for i in input('Введите два числа через пробел: ').split()]
print(f'Число {num} в степени {degree} равно {Exponentiation(num, degree)}')