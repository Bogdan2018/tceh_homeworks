# 6_2 Реализовать декоратор, который измеряет скорость выполнения функций. 
# Написать три разные функции, задекорировать их и проверить
import time


def decorator(function):
    def function_of_measuring_time(*args):
        start_time = time.time()
        function(*args)
        print(function.__name__, time.time() - start_time)

    return function_of_measuring_time


@decorator
def function_1(x, y, z):
    r = x ** y + z
    return r


function_1(6, 5, 4)


@decorator
def function_2(a, z):
    return a ** z


function_2(9, 5)


@decorator
def function_3(a):
    for i in range(a):
        print(a)
    return a


function_3(10)