
areas = [500, 600, 700, 800, 900, 400, 300, 200, 150, 250]


yields = [40, 45, 50, 55, 60, 42, 38, 36, 34, 39]


wheat_production = [area * yield_per_ha for area,
                    yield_per_ha in zip(areas, yields)]


total_wheat = sum(wheat_production)


total_area = sum(areas)


average_yield = total_wheat / total_area


print(f"Общее количество пшеницы, собранное в области: {total_wheat} центнеров.")
print(f"Средняя урожайность по области: {average_yield:.2f} центнеров с гектара.")
