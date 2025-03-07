
import math

def classify_triangle(a, b, c):
  
    if a + b <= c or a + c <= b or b + c <= a:
        return "Треугольник не существует"
    
   
    sides = sorted([a, b, c])
    a, b, c = sides
    
    if a**2 + b**2 == c**2:
        triangle_type = "Прямоугольный"
    elif a**2 + b**2 > c**2:
        triangle_type = "Остроугольный"
    else:
        triangle_type = "Тупоугольный"
        

    if a == b == c:
        features = "Равносторонний"
    elif a == b or a == c or b == c:
        features = "Равнобедренный"
    else:
        features = "Разносторонний"
    
    return f"Треугольник {triangle_type}, {features}"


a = float(input("Введите сторону a: "))
b = float(input("Введите сторону b: "))
c = float(input("Введите сторону c: "))

result = classify_triangle(a, b, c)
print(result)
