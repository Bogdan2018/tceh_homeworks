# 7_1.Реализовать две функции: write_to_file(data) и read_file_data(). 
# Которые соотвественно: пишут данные в файл и читают данные из файла.
def write_to_file(string):
    my_first_file = open('text_1.txt', 'w')
    print('Имя файла', my_first_file.name)
    print('Режим открытия файла', my_first_file.mode)
    my_first_file.write(string)
    my_first_file.close()


write_to_file('это строка будет записана в файл')


def read_file_data():
    my_first_file = open('text_1.txt')
    read_data = my_first_file.read()
    print('Данные из файла')
    print(read_data)
    my_first_file.close()

