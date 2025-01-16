# Ввод числа
number = input("Введите число: ")


if len(number) != 4:
    print("Неверный ввод. Длина должна быть 4.")
else:
    for digit in set(number):
        if number.count(digit) == 3:
            print(f"Число {number} содержит ровно три одинаковые цифры.")
            break
    else:
        print(f"Число {number} не содержит ровно три одинаковые цифры.")
