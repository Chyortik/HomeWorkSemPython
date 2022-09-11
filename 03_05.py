# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

#n = int(input('Введите число: '))

#def get_fibonacci(n):
#    fibo_nums = []
#    a, b = 1, 1
#    for i in range(n):
#        fibo_nums.append(a)
#        a, b = b, a + b
#    a, b = 0, 1
#    for i in range (n):
#        fibo_nums.insert(0, a)
#        a, b = b, a - b
#    return fibo_nums

#fibo_nums = get_fibonacci(n)
#print(get_fibonacci(n))
#print(fibo_nums.index(0))


def fibo(n):
    if n in [1, 2]:                       
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

def nega_fibo(n):
    if n == 1:                       
        return 1
    elif n == 2:                       
        return -1
    else:
        num1, num2 = 1, -1
        for i in range(2, n):
            num1, num2 = num2, num1 - num2
        return num2

list = [0]
userNumber = int(input('Enter any number: '))
for e in range(1, userNumber + 1):
    list.append(fibo(e))
    list.insert(0, nega_fibo(e))
print(list)
