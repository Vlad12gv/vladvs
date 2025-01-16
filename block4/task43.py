def is_divisible(a, b):
    if a % b == 0 or b % a == 0:
        print("Да, одно из чисел является делителем другого")
    else:
        print("Нет, ни одно из чисел не является делителем другого")


a = 6
b = 12
is_divisible(a, b)
