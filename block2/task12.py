number = input('Введите трех значное число: ')
digits = [int(i) for i in number]
a = digits[-1]
b = digits[-2]
v = sum(digits)
print(f'число единиц = {a}, число десятков = {b}, сумма = {v}')
