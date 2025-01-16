a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
c = float(input("Введите третье число: "))
d = float(input("Введите четвертое число: "))


result = sum(x for x in [a, b, c, d] if x > 5)

print(f"Сумма чисел, больших пяти: {result}")
