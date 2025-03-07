
def find_digits_difference(a, b):
    
    result = (20 + a) - (20 + b)
    
   
    c = result // 10
    
   
    d = result % 10
    
    return c, d


a = 3
b = 1
c, d = find_digits_difference(a, b)
print(f"Цифры числа-разности: {c} и {d}")
