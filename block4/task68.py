import math


v0 = float(input("Начальная скорость снаряда (м/с): "))
θ = math.radians(float(input("Угол стрельбы (градусы): ")))
R = float(input("Расстояние до цели (м): "))
H = float(input("Высота цели (м): "))
P = float(input("Высота орудия над землёй (м): "))


t = R / (v0 * math.cos(θ))


y = P + v0 * math.sin(θ) * t - 0.5 * 9.8 * t**2

# Проверка поражения цели
print("Цель" + (" поражена." if y >= H else " не поражена."))
