length_envelope = int(input("Введите длину конверта (мм): "))
width_envelope = int(input("Введите ширину конверта (мм): "))
length_card = int(input("Введите длину открытки (мм): "))
width_card = int(input("Введите ширину открытки (мм): "))


length_card -= 2
width_card -= 2


if (length_card <= length_envelope and width_card <= width_envelope) or \
   (length_card <= width_envelope and width_card <= length_envelope):
    print("Открытка поместится в конверт.")
else:
    print("Открытка не поместится в конверт.")
