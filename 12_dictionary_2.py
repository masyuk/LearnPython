enemy = {
    'loc_x': 70,
    'loc_y': 50,
    'color': 'green',
    'health': 100,
    'name': 'Mudilo',
    'image': ['nice','good','bad']
}

all_enemies = []

for x in range(0,10):
    all_enemies.append(enemy.copy())

print(all_enemies)

for en in all_enemies:
    print(en)
