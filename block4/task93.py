def classify_point(x, y, c):
    if (x <= 0 and y >= 0) or (x > 0 and y <= 0):
        return "I"
    elif (x <= 0 and y <= 0) or (x > 0 and y > 0):
        return "II"
    else:
        return "III"


def main():
    x = float(input("Введите координату X: "))
    y = float(input("Введите координату Y: "))
    c = float(input("Введите значение C: "))
    region = classify_point(x, y, c)
    print(f"Точка ({x:.1f}, {y:.1f}) попадает в область {region}.")


if __name__ == "__main__":
    main()
