
def declension(n, for_1, for_234, for_other):
    d = n % 10

    if d == 1 and n % 100 != 11:
        return for_1

    if d in [2, 3, 4] and not (n % 100 in [12, 13, 14]):
        return for_234

    return for_other


n = int( input('Введите число: ') )

print( 'Мне', n, declension(n, 'год', 'года', 'лет') )
