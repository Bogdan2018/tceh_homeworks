# 6_1 Написать декоратор, который отменяет выполнение 
# функции и пишет: ИМЯ_ФУНКЦИИ не будет вызвана
import time
import random


def decorator(func):
    def wrapper(*args):
        print(func.__name__, 'was not called')

    return wrapper


@decorator
def the_func_will_not_be_colled(a, b):
    return a * b


the_func_will_not_be_colled(7, 8)