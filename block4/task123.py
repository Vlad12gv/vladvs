
import math

def is_rectangular_triangle(a, b, c):
    sides = sorted([a, b, c])
    a, b, c = sides
    if a + b <= c:
        return False
    return a**2 + b**2 == c**2


a = float(input("Введите сторону a: "))
b = float(input("Введите сторону b: "))
c = float(input("Введите сторону c: "))

if is_rectangular_triangle(a, b, c):
    print("Треугольник со сторонами {}, {} и {} является прямоугольным".format(a, b, c))
else:
    print("Треугольник со сторонами {}, {} и {} не является прямоугольным".format(a, b, c))
