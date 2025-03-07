
def check_threats(a, b, c, d):
   
    if a == c or b == d or abs(a - c) == abs(b - d):
        return True
    return False

def check_bishop(a, b, c, d):
    
    if abs(a - c) == abs(b - d):
        return True
    return False

def check_king(a, b, c, d):
    
    if abs(a - c) <= 1 and abs(b - d) <= 1:
        return True
    return False

def check_pawn(a, b, c, d, is_white=True):

    if is_white:
        return abs(a - c) == 0 and b - d == 1
    else:
        return abs(a - c) == 0 and b - d == -1


def check_queen(a, b, c, d):
    return check_threats(a, b, c, d)


def check_all_threats(a, b, c, d, piece_type='Q'):
    if piece_type == 'B':
        return check_bishop(a, b, c, d)
    elif piece_type == 'K':
        return check_king(a, b, c, d)
    elif piece_type == 'P' and b > d: 
        return check_pawn(a, b, c, d, True)
    elif piece_type == 'p' and b < d:  
        return check_pawn(a, b, c, d, False)
    else:
        return check_queen(a, b, c, d)


print("Введите координаты первой фигуры:")
x1 = int(input("X1: "))
y1 = int(input("Y1: "))

print("\nВведите координаты второй фигуры:")
x2 = int(input("X2: "))
y2 = int(input("Y2: "))

piece_type = input("\nУкажите тип фигуры ('Q', 'B', 'K', 'P', 'p'): ").upper()

if check_all_threats(x1, y1, x2, y2, piece_type):
    print(f"Фигура {piece_type} угрожает другой фигуре.")
else:
    print(f"Фигура {piece_type} не угрожает другой фигуре.")
