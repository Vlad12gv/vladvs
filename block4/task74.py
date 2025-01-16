x = float(input("Введите вещественное число: "))

x_abs = x * x
if x_abs < 0:
    x_abs = -x_abs
print(x_abs)
