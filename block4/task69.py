x1 = int(input("x1 = "))
y1 = int(input("y1 = "))
x2 = int(input("x2 = "))
y2 = int(input("y2 = "))
a1 = int(input("ширина1 = "))
b1 = int(input("высота1 = "))
a2 = int(input("ширина2 = "))
b2 = int(input("высота2 = "))


if (x1 <= x2 and x2 <= x1 + a1 and y1 <= y2 and y2 <= y1 + b1):
    print("Пересекаются")
else:
    print("Не пересекаются")
