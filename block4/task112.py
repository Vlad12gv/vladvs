from datetime import date, timedelta


start_date = date(1990, 1, 1)


n = int(input("Введите количество месяцев: "))


end_date = start_date + timedelta(days=n * 30 + 2)


month_names = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"]


print(f"Название месяца: {month_names[end_date.month - 1]}")
