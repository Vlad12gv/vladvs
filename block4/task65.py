def is_leap_year(year):
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)


year = int(input("Введите год: "))
result = "Является" if is_leap_year(year) else "Не является"
print(f"{year} год {result} високосным.")
