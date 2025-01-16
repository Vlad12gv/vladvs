a = int(input("Введите первое целое число: "))
b = int(input("Введите второе целое число: "))
c = int(input("Введите третье целое число: "))

max_num = max(a, b, c)


min_num = min(a, b, c)


mid_num = (a + b + c) - max_num - min_num


print(f"Наибольшее число: {max_num}")
print(f"Наименьшее число: {min_num}")
print(f"Среднее число: {mid_num}")
