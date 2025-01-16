a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
c = float(input("Введите третье число: "))
d = float(input("Введите четвертое число: "))


negative_count = (a < 0) + (b < 0) + (c < 0) + (d < 0)

print(f"Количество отрицательных чисел: {negative_count}")
