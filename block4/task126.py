
def find_mushrooms(k):
    if 11 <= k % 100 <= 14:
        suffix = "грибов"
    else:
        last_digit = k % 10
        if last_digit == 1:
            suffix = "гриб"
        elif 2 <= last_digit <= 4:
            suffix = "гриба"
        else:
            suffix = "грибов"
    return f"мы нашли {k} {suffix} в лесу"


k = int(input("Введите количество грибов: "))
print(find_mushrooms(k))
