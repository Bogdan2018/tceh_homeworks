# 7_2.Реализовать следующую логику: 
# получать при помощи requests данные сайта https://jsonplaceholder.typicode.com/, 
# выводить в консоль все пары "ключ-значение", сохранять полученный json в файл.


import requests
import json

try:
    responce_of_site = requests.get('https://jsonplaceholder.typicode.com/')
    responce_of_site.raise_for_status()
except responce_of_site.exceptions.ConnectionError:
    print('ConnectionError')

file_dict = open('file_dict.txt', 'w')
file_dict.write(json.dumps(dict(responce_of_site.headers)))
file_dict.close()