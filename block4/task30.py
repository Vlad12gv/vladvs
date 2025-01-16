def check_conditions(number):
    hundreds = number // 100
    tens = (number // 10) % 10
    units = number % 10

    digit_sum = hundreds + tens + units

    digit_product = hundreds * tens * units

    conditions = {
        "а": 10 <= digit_sum <= 99,
        "б": 100 <= digit_product <= 999,
        "в": digit_product > number,
        "г": digit_sum % 5 == 0,
        "д": digit_sum % number == 0
    }
    return conditions


three_digit_number = int(input("Введите трехзначное число: "))

results = check_conditions(three_digit_number)

for key, value in results.items():
    print(f"{key}: {value}")
