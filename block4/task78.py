x1 = int(input("Введите первое число: "))
x2 = int(input("Введите второе число: "))
x3 = int(input("Введите третье число: "))


even_numbers = [x1, x2, x3]

for x in even_numbers:
    if x % 2 == 0:
        print(x, end=" ")
