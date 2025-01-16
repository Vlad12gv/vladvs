data = (
    (60, "легкий вес"),
    (64, "первый полусредний вес"),
    (69, "полусредний вес"),
)


x = int(input("Введите число: "))

for weight, rank in data:
    if x < weight:
        print(rank)
        break
else:
    print("вне условия")
