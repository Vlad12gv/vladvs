num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
num3 = float(input("Введите третье число: "))


numbers = sorted([num1, num2, num3], reverse=True)


two_largest_sum = numbers[0] + numbers[1]


print(f"Сумма двух наибольших чисел: {two_largest_sum}")
