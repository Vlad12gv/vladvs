a = int(input("Введите первое целое число: "))
b = int(input("Введите второе целое число: "))
c = int(input("Введите третье целое число: "))
d = int(input("Введите четвертое целое число: "))

even_count = ((a % 2 == 0) + (b % 2 == 0) + (c % 2 == 0) + (d % 2 == 0))

print(f"Количество чётных чисел: {even_count}")
