
colors = ['Зеленый', 'Красный', 'Желтый', 'Белый', 'Черный']


animals = [
    'Крыса', 'Корова', 'Тигр', 'Заяц', 'Дракон', 'Змея', 'Лошадь', 'Овца', 'Обезьяна', 'Петух', 'Собака', 'Свинья'
]

def chinese_calendar(n):
    
    cycle_start = 1984
    
    
    position = (n - cycle_start) % 60
    
    
    color_index = position // 12
    color = colors[color_index]
    
   
    animal_index = position % 12
    animal = animals[animal_index]
    
    return f'{animal}, {color}'


print(chinese_calendar(1984)) 


n = int(input("Введите год: "))
print(chinese_calendar(n))
