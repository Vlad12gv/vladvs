a = float(input('Введите сторону A: '))
b = float(input('Введите сторону B: '))
c = float(input('Введите сторону C: '))
d = float(input('Введите сторону D: '))

if ((a <= c) and (b <= d)) or ((a <= d) and (b <= c)):
    print('Да, может')
else:
    print('Нет, не может')
