# 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу
# между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 10.01] => 0.19


# 1
#my_list = [1.1, 1.2, 3.1, 5, 10.01]
#min = 1
#max = 0
#for i in my_list:
#    if (i - int(i)) <= min:
#        min = i - int(i)
#    if (i - int(i)) >= max:
#        max = i - int(i)  
#print(max-min)

# 2
lst = list(map(float, input("Введите числа через пробел:\n").split()))
new_lst = [round(i%1,2) for i in lst if i%1 != 0]
print(max(new_lst) - min(new_lst))
