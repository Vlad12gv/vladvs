
def is_sum_even(a, n):
    total_sum = 0
    for i in range(n):
        total_sum += a + i
    return total_sum % 2 == 0


a = int(input("Введите начальный номер квартиры: "))
n = int(input("Введите количество квартир: "))

if is_sum_even(a, n):
    print("Сумма номеров всех квартир является четной.")
else:
    print("Сумма номеров всех квартир является нечетной.")
