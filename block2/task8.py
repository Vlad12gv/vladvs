def day_of_week(k, starting_day):
    return (starting_day + (k - 1)) % 7

k = int(input("Введите какой день в году (1-365): "))
starting_day = int(input("Введите день недели для 1 января (0 - понедельник, 1 - вторник, ..., 6 - воскресенье): "))

if 1 < k < 365 and 0 <= starting_day <= 6:
    day_n = day_of_week(k, starting_day)
    print(f"{k}-й день года приходится на: {day_n}")
else:
    print("Некорректные вводные данные.")

print(day_of_week)
