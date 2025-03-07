
def can_move(a, b, c, d, e, f, white_piece, black_piece):
    def rook(a, b, c, d): 
        return a == c or b == d
    
    def bishop(a, b, c, d): 
        return abs(a - c) == abs(b - d)
    
    def queen(a, b, c, d): 
        return rook(a, b, c, d) or bishop(a, b, c, d)
    
    def knight(a, b, c, d): 
        return abs(a - c) * abs(b - d) in [2, 6]
    
    def king(a, b, c, d): 
        return max(abs(a - c), abs(b - d)) == 1
    
    move_funcs = {
        'rook': lambda a, b, e, f: a == e or b == f,
        'bishop': lambda a, b, e, f: abs(a - e) == abs(b - f),
        'queen': lambda a, b, e, f: a == e or b == f or abs(a - e) == abs(b - f),
        'knight': lambda a, b, e, f: abs(a - e) * abs(b - f) in [2, 6],
        'king': lambda a, b, e, f: max(abs(a - e), abs(b - f)) == 1
    }
    
    attack_funcs = {
        'rook': rook,
        'bishop': bishop,
        'queen': queen,
        'knight': knight,
        'king': king
    }
    
    return move_funcs[white_piece](a, b, e, f) and not attack_funcs[black_piece](c, d, e, f)

# Ввод данных пользователем
a = int(input("Введите координату a: "))
b = int(input("Введите координату b: "))
c = int(input("Введите координату c: "))
d = int(input("Введите координату d: "))
e = int(input("Введите координату e: "))
f = int(input("Введите координату f: "))
white_piece = input("Введите тип белой фигуры (rook, bishop, queen, knight, king): ")
black_piece = input("Введите тип чёрной фигуры (rook, bishop, queen, knight, king): ")

if can_move(a, b, c, d, e, f, white_piece, black_piece):
    print("Белая фигура может пойти на поле (e, f)")
else:
    print("Белая фигура не может пойти на поле (e, f)")
