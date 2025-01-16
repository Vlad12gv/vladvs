import math
a = float(input("Введите число А: "))
x = a

if x <= 0:
    fx = 0
    print("x <= 0,2 <= x <= 0,9; f(a) = ", fx)
elif 0 < x < 1:
    fx = x
    print("-2,4 <= x <= 5,7; f(a) = ", fx)
else:
    fx = math.pow(x, 1)
    print("x >= 1; f(a) = ", fx)
