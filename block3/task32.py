def is_in_shaded_area(x, y):

    if -2 <= x <= 1 and 0 <= y <= (x + 1) ** 2:
        return True

    if -2 <= x <= 1 and 0 <= y <= x + 2:
        return True

    if 0 <= x <= 2 and 0 <= y <= x**0.5:
        return True

    if 0 < x <= 2 and 0 < y <= 4 / x:
        return True

    return False

X = float(input("Введите значение X: "))
y = float(input("Введите значение y: "))

if is_in_shaded_area(X, y):
    print(f"Точка ({X}, {y}) находится в заштрихованной области.")
else:
    print(f"Точка ({X}, {y}) не находится в заштрихованной области.")
