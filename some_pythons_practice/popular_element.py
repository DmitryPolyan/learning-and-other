"""
Дан массив a из n целых чисел. Напишите программу, которая найдет число, которое чаще других встречается в массиве.
Ограничение времени: 2 с, ограничение памяти: 256 МБ.

Формат ввода
В первой строке входных данных записано число n (1 ≤ n ≤ 300 000).
Во второй строке записаны n целых чисел ai (0 ≤ ai ≤ 1 000 000 000).

Формат вывода
Выведите единственное число x, наибольшее из чисел, которое чаще других встречается в массиве a.
"""
import time
import random

def bigger_max_elmnt(n: int) -> int:
    """
    ф-я поиска наибольшего из чисел, которое чаще других встречается в массиве a.
    :param n: Кол-во эл-тов в массиве
    :return: Самое большое из чаще встречающихся чисел
    """
    maxs = 0
    element = None
    a = [random.randint(0, 1000) for i in range(0, n)]
    slovar = dict()
    for i in a:
        slovar[i] = slovar.get(i, 0) + 1
        if slovar[i] > maxs or slovar[i] == maxs and i > element:
            maxs = slovar[i]
            element = i
    return element


if __name__ == '__main__':
    start = time.time()
    print(bigger_max_elmnt(12))
    print(time.time() - start)
