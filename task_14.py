# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N

n = int(input('Введите число n '))
num = 0
a = 2
for i in range(n):
    if num != 1:
        a = a ** i
        if a <= n:
            print(a)
            a = 2
        else:
            num = 1
    else:
        i = n