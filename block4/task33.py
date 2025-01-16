n = int(input("Введите натуральное число: "))


last_digit = n % 10


even_ending = last_digit % 2 == 0
odd_ending = not even_ending

print(f"Число {n} заканчивается чётной цифрой: {even_ending}")
print(f"Число {n} заканчивается нечётной цифрой: {odd_ending}")
