def is_rook_threat(a, b, c, d):
    return a == c or b == d


def is_bishop_threat(a, b, c, d):
    return abs(a - c) == abs(b - d)


def is_king_threat(a, b, c, d):
    return abs(a - c) <= 1 and abs(b - d) <= 1


def is_queen_threat(a, b, c, d):
    return is_rook_threat(a, b, c, d) or is_bishop_threat(a, b, c, d)


def is_white_pawn_move_normal(a, b, c, d):
    return a + 1 == c and b == d


def is_white_pawn_capture(a, b, c, d):
    return a + 1 == c and abs(b - d) == 1


if __name__ == "__main__":
    a = int(input("Введите координату a: "))
    b = int(input("Введите координату b: "))
    c = int(input("Введите координату c: "))
    d = int(input("Введите координату d: "))

    if is_rook_threat(a, b, c, d):
        print("Ладья угрожает")

    if is_bishop_threat(a, b, c, d):
        print("Слон угрожает")

    if is_king_threat(a, b, c, d):
        print("Король угрожает")

    if is_queen_threat(a, b, c, d):
        print("Ферзь угрожает")

    if is_white_pawn_move_normal(a, b, c, d):
        print("Белая пешка может пойти обычным ходом")

    if is_white_pawn_capture(a, b, c, d):
        print("Белая пешка может побить фигуру или пешку соперника")

print(a)
