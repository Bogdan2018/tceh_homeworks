# 5_1. Написать списковые выражения, которые:
import random, collections

# a.создают список из строк всех нечетных чисел от 1 до 100
list = [str(i) for i in range(1, 100, 2)]
# b.создают список из объектов другого списка, кроме итерируемых 
list_objects = [1, 3, ('dd', 'ff'), None, 's']
new_list = [i for i in list_objects if isinstance(i, collections.Iterable)]

# c.создают список из фразы 'The quick brown fox jumps over the lazy dog', 
# где каждый объект списка - кортеж из: слова в верхнем регистре, 
# слова в случанйном регистре (qUIcK) и длины слова

old_list = 'The quick brown fox jumps over the lazy dog'
new_list = [(i.upper(), ''.join([random.choice([j.lower(), j.upper()]) for j in i]), len(i)) for i in
            old_list.split(' ')]
