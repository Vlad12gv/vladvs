
def find_kth_digit(k):
    
    first_part_digits = 49 * 2 
    
    
    if k <= first_part_digits:
        number = 50 + ((k - 1) // 2)  
        digit_position = (k - 1) % 2  
        return str(number)[digit_position]
    
    
    else:
        k -= first_part_digits  
        number = 99 + ((k - 1) // 3) 
        digit_position = (k - 1) % 3  
        return str(number)[digit_position]


k = int(input("Введите значение k (1 <= k <= 551): "))
result = find_kth_digit(k)
print(f"k-я цифра: {result}")
