import math


def solve_quadratic(a, b, c):
    D = b**2 - 4*a*c

    if D > 0:
        x1 = (-b - math.sqrt(D)) / (2 * a)
        x2 = (-b + math.sqrt(D)) / (2 * a)
        return f"Корни уравнения: {x1}, {x2}"
    elif D == 0:
        x = -b / (2 * a)
        return f"Корень уравнения: {x} (корни совпадают)"
    else:
        return "Действительных корней нет"


a = float(input("Введите коэффициент a: "))
b = float(input("Введите коэффициент b: "))
c = float(input("Введите коэффициент c: "))
print(solve_quadratic(a, b, c))
