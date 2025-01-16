number = int(input("Введите двузначное число: "))


contains_4_or_7 = '4' in str(number) or '7' in str(number)


if contains_4_or_7:
    print("Цифры 4 или 7 входят в число.")
else:
    print("Цифры 4 или 7 не входят в число.")
