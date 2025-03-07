
from datetime import date

def compare_birthdays(year1, month1, day1, year2, month2, day2):
    birthdate1 = date(year1, month1, day1)
    birthdate2 = date(year2, month2, day2)
    
    if birthdate1 < birthdate2:
        return "Первый человек старше."
    elif birthdate1 > birthdate2:
        return "Второй человек старше."
    else:
        return "Люди родились в один день."


year1 = int(input("Введите год рождения первого человека: "))
month1 = int(input("Введите месяц рождения первого человека: "))
day1 = int(input("Введите день рождения первого человека: "))

year2 = int(input("Введите год рождения второго человека: "))
month2 = int(input("Введите месяц рождения второго человека: "))
day2 = int(input("Введите день рождения второго человека: "))

result = compare_birthdays(year1, month1, day1, year2, month2, day2)
print(result)
