def is_happy_number(num):
    return sum(map(int, str(num)[:3])) == sum(map(int, str(num)[3:]))


num = int(input("Введите шестизначное число: "))
print("Счастливое число!" if is_happy_number(num) else "Обычное число.")
