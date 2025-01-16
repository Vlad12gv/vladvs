def y(x):
    if x < -1:
        return -1 / x
    elif x <= 10:
        return x ** 2
    else:
        return -1


x = float(input("Введите значение x: "))
result = y(x)
print(f"Значение функции y(x) при x={x} равно {result}")
