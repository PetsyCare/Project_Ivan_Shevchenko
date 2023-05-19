#ДЗ на понедельник (Ivanov_Lesson_16.py) - скидывает на гитхаб
# Напишите функцию modify_list(l), которая принимает на вход список целых чисел, удаляет из него все нечётные значения, а чётные нацело делит на два. Функция не должна ничего возвращать, требуется только изменение переданного списка, например:

# импортируем randint для генерации случайных чисел
from random import randint

print('Task 16:')

# генерируем случайный список целых чисел
lst = [randint(1,100) for i in range(randint(1,15))]

print(f'Original list: \t{lst}')

# создаем пользовательскую функцию
def modify_list(list_int):
    list_id = 0
    while len(list_int) > list_id:
        if list_int[list_id] % 2 != 0:
            del list_int[list_id]
            list_id -= 1
        else:
            list_int[list_id] = int(list_int[list_id] / 2)
        list_id += 1
    return list_int

# выводим результат
print(f'\nResult: \t\t{modify_list(lst)}')