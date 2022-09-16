#4. Задана натуральная степень k. Сформировать случайным образом список #коэффициентов
#(значения от 0 до 100) многочлена и записать в файл многочлен степени k.
#Пример: k=2 => 2*x? + 4*x + 5 = 0 или x? + 5 = 0 или 10*x? = 0
#4.1
import random
def write_file(st):
    with open('Task04_04.txt', 'w') as data:
        data.write(st)
def rnd():
    return random.randint(0,101)
def create_mn(k):
    lst = [rnd() for i in range(k+1)]
    return lst
    
def create_str(sp):
    lst= sp[::-1]
    wr = ''
    if len(lst) < 1:
        wr = 'x = 0'
    else:
        for i in range(len(lst)):
            if i != len(lst) - 1 and lst[i] != 0 and i != len(lst) - 2:
                wr += f'{lst[i]}x^{len(lst)-i-1}'
                if lst[i+1] != 0:
                    wr += ' + '
            elif i == len(lst) - 2 and lst[i] != 0:
                wr += f'{lst[i]}x'
                if lst[i+1] != 0:
                    wr += ' + '
            elif i == len(lst) - 1 and lst[i] != 0:
                wr += f'{lst[i]} = 0'
            elif i == len(lst) - 1 and lst[i] == 0:
                wr += ' = 0'
    return wr

k = int(input("Введите натуральную степень k = "))
koef = create_mn(k)
write_file(create_str(koef))

#4.2

from random import randint
import itertools

k = randint(2, 7)

def get_ratios(k):
    ratios = [randint(0, 100) for i in range (k + 1)]
    while ratios[0] == 0:
        ratios[0] = randint(1, 100) 
    return ratios

def get_polynomial(k, ratios):
    var = ['*x^']*(k-1) + ['*x']
    polynomial = [[a, b, c] for a, b, c  in itertools.zip_longest(ratios, var, range(k, 1, -1), fillvalue = '') if a !=0]
    for x in polynomial:
        x.append(' + ')
    polynomial = list(itertools.chain(*polynomial))
    polynomial[-1] = ' = 0'
    return "".join(map(str, polynomial)).replace(' 1*x',' x')

ratios = get_ratios(k)
polynom1 = get_polynomial(k, ratios)
print(polynom1)

with open('Task04_04.txt', 'w') as data:
    data.write(polynom1)

print('Второй многочлен для следующей задачи:')

k = randint(2, 5)
ratios = get_ratios(k) 
polynom2 = get_polynomial(k, ratios)
print(polynom2)
with open('Task04_041.txt', 'w') as data:
    data.write(polynom2)
