n = int(input("Введите трехзначное число: "))


digits = str(n)


if '4' in digits or '7' in digits:
    print("Да, в числе есть цифра 4 или 7")
else:
    print("Нет, в числе нет цифр 4 или 7")

if '3' in digits or '6' in digits or '9' in digits:
    print("Да, в числе есть цифра 3, 6 или 9")
else:
    print("Нет, в числе нет цифр 3, 6 или 9")
