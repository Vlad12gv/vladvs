
def find_digits_difference(a, b):
    
    result = 20 + a - b
    
    
    c = result // 10
    
   
    d = result % 10
    
    return c, d


a = 3
b = 5
c, d = find_digits_difference(a, b)
print(f"Цифры числа-разности: {c} и {d}")
