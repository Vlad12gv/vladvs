
Time_Left = int(input("введите время в минутах с начала часа: "))
 

x = Time_Left // 5
 

l = Time_Left - (x * 5)
 
if l == 0:
    print('это красный')
elif l == 1:
    print('это зелённый')
elif l == 2:
    print('это зелёный')
elif l == 3:
    print('это зелённый')
elif l == 4:
    print('это красный')
elif l == 5:
    print('это красный')
