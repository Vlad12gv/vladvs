def is_square_equal_to_four_times_cubes_sum(n):
    # Проверка, что n является двузначным числом
    if not (10 <= n <= 99):
        return False

    a = n // 10  # первая цифра
    b = n % 10   # вторая цифра

    square_of_n = n ** 2

    four_times_cubes_sum = 4 * (a**3 + b**3)

    # Сравниваем результаты
    return square_of_n == four_times_cubes_sum

print(is_square_equal_to_four_times_cubes_sum(48))
print(is_square_equal_to_four_times_cubes_sum(52))

