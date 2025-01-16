def absolute_value(x):
    if x < 0:
        x = -x
    return x


x1 = float(input("Введите первое число: "))
x2 = float(input("Введите второе число: "))

x1 = absolute_value(x1)
x2 = absolute_value(x2)


print((x1 + x2) / 2)


print((x1 * x2) ** 0.5)
