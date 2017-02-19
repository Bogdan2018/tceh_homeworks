# 6_4 Написать генератор, который возвращает
# бесконечную последовательность случайных чисел, 
# таких что следующее не меньше прошлого
import random, sys


def random_element():
    min_digit = sys.minsize
    while min_digit < sys.maxsize:
        min_digit = random.uniform(min_digit, sys.maxsize)
        yield min_digit


g = random_element()
for i in g:
    print(i)