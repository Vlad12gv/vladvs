a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
c = float(input("Введите третье число: "))


max_value = a if a > b else b
max_value = max_value if max_value > c else c


min_value = a if a < b else b
min_value = min_value if min_value < c else c


print(f"Максимальное значение: {max_value}")
print(f"Минимальное значение: {min_value}")
