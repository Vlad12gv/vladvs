def is_in_shaded_area(x, y):

    condition_a = (-2 <= x <= 1) and (0 <= y <= -(x + 1)**2 + 4)

    condition_b = (x >= -3) and (0 <= y <= -(1/9)*(x + 3)**2 + 6)

    return condition_a or condition_b

x = float(input("Введите значение x: "))
y = float(input("Введите значение y: "))

if is_in_shaded_area(x, y):
    print(f"Точка ({x}, {y}) находится в заштрихованной области.")
else:
    print(f"Точка ({x}, {y}) не находится в заштрихованной области.")
