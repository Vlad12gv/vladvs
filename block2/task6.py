sek = int(input('Сколько секунд прошло с начала суток?'))

hour = sek/3600
minute = hour/60
sek = minute/60

print(f'Вот столько времени прошло: {hour}, {minute}, {sek}')
