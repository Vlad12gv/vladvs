def is_palindrome(number):
    if not (100 <= number <= 999):
        return False

    hundreds_digit = number // 100  # сотня
    units_digit = number % 10       # единицы

    return hundreds_digit == units_digit

print(is_palindrome(121))
print(is_palindrome(123))
print(is_palindrome(101))
