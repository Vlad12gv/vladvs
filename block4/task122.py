
def is_triangle_exists(a, b, c):
    return a + b > c and a + c > b and b + c > a


a = float(input("Введите сторону a: "))
b = float(input("Введите сторону b: "))
c = float(input("Введите сторону c: "))

if is_triangle_exists(a, b, c):
    print("Треугольник со сторонами {}, {} и {} существует".format(a, b, c))
else:
    print("Треугольник со сторонами {}, {} и {} не существует".format(a, b, c))
