
import datetime

def get_previous_day(g, m, n):
    prev_date = datetime.date(g, m, n) - datetime.timedelta(days=1)
    return prev_date

def get_next_day(g, m, n):
    next_date = datetime.date(g, m, n) + datetime.timedelta(days=1)
    return next_date

# Пример использования
g = int(input("Введите год: "))
m = int(input("Введите номер месяца: "))
n = int(input("Введите число: "))

prev_day = get_previous_day(g, m, n)
next_day = get_next_day(g, m, n)

print(f"Дата предыдущего дня: {prev_day}")
print(f"Дата следующего дня: {next_day}")
