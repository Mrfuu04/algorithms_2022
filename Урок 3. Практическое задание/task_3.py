"""
Задание 3.
Определить количество различных (уникальных) подстрок
с использованием хеш-функции.
Дана строка S длиной N, состоящая только из строчных латинских букв.

Подсказка: вы должны в цикле для каждой подстроки вычислить хеш
Все хеши записываем во множество.
Оно отсечет дубли.

Экономия на размере хранимых данных (для длинных строк) и
скорость доступа вместе с уникальностью элементов,
которые даёт множество, сделают решение коротким и эффективным.

Пример:
рара - 6 уникальных подстрок

рар
ра
ар
ара
р
а
"""

import hashlib


def get_unique_hash(s, set):
    """Функция формирует хэш из подстрок строки - s
    и передает во множество - set
    """
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            if s[i: j] == s:
                pass
            else:
                my_set.add(hashlib.sha256(s[i: j].encode('utf-8')).hexdigest())
    return set


my_set = set()
s = 'papa'
s2 = 'He1l0'

print(len(get_unique_hash(s, my_set)))
print(len(get_unique_hash(s2, my_set)))
