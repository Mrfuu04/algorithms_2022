"""
Задание 1.

Реализуйте:

a) заполнение списка, оцените сложность в O-нотации.
   заполнение словаря, оцените сложность в O-нотации.
   сделайте аналитику, что заполняется быстрее и почему.
   сделайте замеры времени.

b) выполните со списком и словарем операции: изменения и удаления элемента.
   оцените сложности в O-нотации для операций
   получения и удаления по списку и словарю
   сделайте аналитику, какие операции быстрее и почему
   сделайте замеры времени.


ВНИМАНИЕ: в задании два пункта - а) и b)
НУЖНО выполнить оба пункта

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)
вы уже знаете, что такое декоратор и как его реализовать,
обязательно реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к своим функциям!
"""

from time import time


def time_check(func):
    """Функция-декоратор для замера времени выполенения функции"""
    def wrapper(*args, **kwargs):
        start = time()
        func(*args, **kwargs)
        print(f'Время выполнения функции {func.__name__} = {time() - start} секунд')

    return wrapper


# Задания из подпункта a)

@time_check
def full_massive(massive_name, key=0, *args, **kwargs):
    """Заполнение массивова. Сделал одной фукнцией, чтобы не городить огород.
    key == 1 - заполнение словаря
    key == anykey - заполнение списка
    """
    if key == 1:                       # Заполнение словаря
        for k, v in kwargs.items():    # Сложность O(n)
            massive_name[k] = v        # Cложность O(1)
        return massive_name
    else:                              # Заполнение списка
        for i in args:                 # Сложность O(n)
            massive_name.append(i)     # Сложность O(1)
    return massive_name


my_dict = {}
my_list = []
full_massive(my_dict, key=1, **{str(key):key for key in range(100000)})
full_massive(my_list, *(i for i in range(100000)))
# Не смотря на одинаковую оценку сложности по О-нотации
# словари заполняются дольше т.к словари реализуются с помощью хэш-таблиц


# Задания из подпункта b)

@time_check
def change_dict(dict, keyword=None, key=0, **kwargs):
    """key = 1 - удаление
    key = anyKey - изменение
    keyword используется для удаления по ключу"""
    if key == 1:
        if isinstance(keyword, tuple): # O(1)
            for k in keyword:          # O(n)
                dict.pop(k)            # O(1)
        else:
            dict.pop(keyword)          # O(1)
    else:
        for k, v in kwargs.items():    # O(n)
            dict[k] = v                # O(1)


@time_check
def change_list(list, keyword=None, change=None, key=0):
    """key = 1 - удаление
    key = anyKey - изменение
    keyword используется для удаления
    change - слово на замену"""
    if key == 1:
        list.remove(keyword)          # O(n)
    else:
        list[keyword] = change        # O(n)


print(my_dict.get('99999'))
change_dict(my_dict, key=1, keyword='99999')
print(my_dict.get('99999'))


print(my_list[-1])
change_list(my_list, key=1, keyword=my_list[-1])
print(my_list[-1])


# Вывод: работа со словарями быстрее т.к обращение к ключам происходит со сложность O(1)
# что в случае со списками практически всегда идет проход по всему списку O(n)