
# a=55
# b=879
# m="2522"
# print("введите число")
# n = int(input()) 
# print(n+10)
# s=8<9
# print(s)
# n = int(input())
# if n % 2 == 0 and n % 3 == 0:
#   print('Число кратно 6')




# Задача №1. Решение в группах
# Семинар 1. Ввод-вывод, операторы ветвления
# За день машина проезжает n километров. Сколько
# дней нужно, чтобы проехать маршрут длиной m
# километров? При решении этой задачи нельзя
# пользоваться условной инструкцией if и циклами.
# Input:
# n = 700 за день
# m = 750 
# Output:
# 2

from math import ceil
# n = 700
# m = 750

# # print((n + m - 1)//n)
# # print(ceil(m / n))
# print(n+m-1//n)


# Решение в группах
# В некоторой школе решили набрать три новых
# математических класса и оборудовать кабинеты для
# них новыми партами. За каждой партой может сидеть
# два учащихся. Известно количество учащихся в
# каждом из трех классов. Выведите наименьшее
# число парт, которое нужно приобрести для них.
# Input: 20 21 22(ввод чисел НЕ в одну строку)
# Output: 32

# a, b, c= 20, 21, 22
# print(a//2+a%2+b//2+b%2+c//2+c%2)
# a=0


# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N

N = int(input("введите число"))
k = 0
while 2**k <= N:
    print(2**k, end=" ")
    k += 1
print()
