def is_in_I(x, y):
    return (x <= 0 and y >= 0) or (x > 0 and y <= 0)


def is_in_II(x, y):
    return (x <= 0 and y <= 0) or (x > 0 and y > 0)


def is_in_III(x, y):
    return not is_in_I(x, y) and not is_in_II(x, y)


if __name__ == "__main__":

    x = 4
    y = 8

    if is_in_I(x, y):
        print("Точка (%d, %d) попадает в область I." % (x, y))
    elif is_in_II(x, y):
        print("Точка (%d, %d) попадает в область II." % (x, y))
    else:
        print("Точка (%d, %d) попадает в область III." % (x, y))
