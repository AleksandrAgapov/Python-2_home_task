#Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.

x = int(input('Введите первое натуральное число X от 1 до 1000 '))
y = int(input('Введите второе натуральное число Y от 1 до 1000 '))
if x < 1 or x > 1000 or y < 1 or y > 1000:
    print('Вы ввели число не из заданного диапазона!')
else:
    S = x + y
    P = x * y
    a = 0
    for i in range(1001):
        if a != 1:
            for j in range(1001):
                if a != 1:
                    if i * j == P and i + j == S:
                        print(i, j)
                        a = 1
            else:
                j = 1001
        else:
            i = 1001