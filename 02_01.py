# 1. Напишите программу, которая принимает на вход вещественное число
# и показывает сумму его цифр.
# Пример:
# 0,56 -> 11

num = float(input('Введите число: '))
def sum_nums(num):
    sum = 0
    for i in str(num):
        if i != ".":
            sum += int(i)
    return sum

print(f'Сумма цифр числа = {sum_nums(num)}')