# 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# 1
#my_list = [2, 3, 5, 6]
#result_list = []
#for i in range((len(my_list)+1)//2):
#    result_list.append(my_list[i]*my_list[len(my_list)-1-i])
#print(result_list)

# 2
def mult_lst(lst):
    l = len(lst)//2 + 1 if len(lst) % 2 != 0 else len(lst)//2
    new_lst = [lst[i]*lst[len(lst)-i-1] for i in range(l)]
    print(new_lst)

#lst = [2, 3, 4, 5, 6]
#mult_lst(lst)
lst = list(map(int, input("Введите числа через пробел:\n").split()))
mult_lst(lst)