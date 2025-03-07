
def skl(w, lst) :
    f1 = lambda a: (a%100)//10 != 1 and a%10 == 1
    f2 = lambda a: (a%100)//10 != 1 and a%10 in [2,3,4]
    return lst[0] if f1(w) else  lst[1] if f2(w) else lst[2]
 

months = ['месяц', 'месяца', 'месяцев']
years = ['год', 'года', 'лет']
y, m = divmod(int(input()), 12)
yres = f'{y} {skl(y, years)} ' if y else ''
mres = f'{m} {skl(m, months)}' if m else 'ровно'
print(yres + mres)
