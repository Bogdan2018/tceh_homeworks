# 6_5 Написать генератор, который принимает 
# на вход дату и на каждый вызов выдает следующий день
import datetime


def generator_date():
    now_day = datetime.date.today()
    while True:
        try:
            if now_day.month == 12:
                now_day = now_day.replace(year=now_day.year + 1, month=1, day=1)
                yield now_day
            else:
                now_day = now_day.replace(day=now_day.day + 1)
                yield now_day
        except ValueError:
            now_day = now_day.replace(month=now_day.month + 1, day=1)
            yield now_day


for i in generator_date():
    print(i)