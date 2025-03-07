
def find_kth_digit(k):

    one_digit_count = 9    
    two_digit_count = 90   
    three_digit_count = 11  


    one_digit_length = one_digit_count * 1
    two_digit_length = two_digit_count * 2
    three_digit_length = three_digit_count * 3


    if k <= one_digit_length:
        number = k
    elif k <= one_digit_length + two_digit_length:
        k -= one_digit_length
        number = 10 + (k - 1) // 2
    else:
        k -= one_digit_length + two_digit_length
        number = 100 + (k - 1) // 3


    position_in_number = (k - 1) % len(str(number))
    return int(str(number)[position_in_number])


k = int(input("Введите значение k (1 <= k <= 222): "))
result = find_kth_digit(k)
print(f"{k}-я цифра: {result}")
