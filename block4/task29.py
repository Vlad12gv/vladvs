N = int(input("Введите трехзначное число: "))


a = N // 100
b = (N // 10) % 10
c = N % 10


square_of_N = N * N


sum_of_cubes = a**3 + b**3 + c**3


if square_of_N == sum_of_cubes:
    print("Квадрат числа равен сумме кубов его цифр.")
else:
    print("Квадрат числа не равен сумме кубов его цифр.")
