# 6_3 Написать генероторное выражение, 
# которое включает в себя все четные числа от 0 до 100
generator = (i for i in range(0, 100, 2))
exemplar_generator = generator
for i in exemplar_generator:
    print(i)
