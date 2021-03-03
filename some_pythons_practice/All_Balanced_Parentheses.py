"""

Write a function that makes a list of strings
representing all the ways you can balance n pairs of parentheses.
"""

import itertools

    
def get_variants(n: int) -> int:
    """
    Ф-я перебора возможных вариантов расположения скобок
    :param n: Кол-во пар скобок
    """
    ways = 0
    variants_list = list(set(itertools.permutations('()'*n, n*2)))
    for i in variants_list:
        counter = 0
        for j in i:
            if j == '(':
                counter += 1
            else:
                counter -= 1
                if counter < 0:
                    variants_list.remove(i)
                    break
        else:
            ways += 1
            print(''.join(i))
    return ways


if __name__ == '__main__':
    x = int(input('Enter number - '))
    print('ways of balance is', get_variants(x))

