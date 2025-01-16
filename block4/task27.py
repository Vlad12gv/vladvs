x = int(input("Введите трёхзначное число: "))
x1 = x
x2 = 0

while x > 0:
    x, y = divmod(x, 10)
    x2 = x2*10 + y
print("не" if x1 != x2 else "", "является")
