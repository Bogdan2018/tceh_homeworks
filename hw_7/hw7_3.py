# 7_3.Обратиться с странице https://habrahabr.ru/. Получить текст страницы. 
# При помощи регулярных выражений нужно получить все ссылки со страницы на другие.
import re
import requests


def search_engine(url):
    response_of_site = requests.get(url)
    site_text = response_of_site.content
    result = re.findall(r'<a href="(https?://.*?)"', str(site_text))
    print(result)


if __name__ == '__main__':
    search_engine('https://habrahabr.ru/')
