#Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.

S = int(input('Введите сумму чисел S от 1 до 1000 '))
P = int(input('Введите произведение этих же чисел P от 1 до 1000 '))
if S < 1 or S > 1000 or P < 1 or  P > 1000:
    print('Вы ввели число не из заданного диапазона!')
else:
   
    a = 0
    for i in range(1001):
        if a != 1:
            for j in range(1001):
                if a != 1:
                    if i * j == P and i + j == S:
                        print(f"вы загадали числа {i, j}")
                        a = 1
                        
            else:
                j = 1001
        else:
            i = 1001