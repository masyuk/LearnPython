#    (----Item----)
#    (key)  (value)
enemy = {
    'loc_x': 70,
    'loc_y': 50,
    'color': 'green',
    'health': 100,
    'name': 'Mudilo'
}

print(enemy)
print(enemy['name'])

enemy['rank'] = 'Noob'
print(enemy)

del enemy['rank']
print(enemy)

print('--------------')
enemy['loc_x'] += 40

