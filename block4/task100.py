num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
num3 = float(input("Введите третье число: "))

numbers = sorted([num1, num2, num3])


product_of_two_smallest = numbers[0] * numbers[1]


print(f"Произведение двух наименьших чисел: {product_of_two_smallest}")
