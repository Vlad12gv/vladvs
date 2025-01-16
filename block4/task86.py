def z(a):
    if a > 0:
        return 1
    elif a < 0:
        return -1
    else:
        return 0


a = float(input("Введите значение a: "))
result = z(a)
print(f"Значение функции z(a) при a={a} равно {result}")
