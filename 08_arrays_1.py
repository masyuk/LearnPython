cities = ['NY', 'kharkiv', 'Kiev']

print(cities)
print(len(cities))
print(cities[0])
print(cities[-1])
print(cities[1].title())

print('---------')
cities.sort()
print(cities)

print('---------')
cities.append('Rovno')
print(cities)

print('---------')
del cities[0]
print(cities)

print('---------')
cities.remove('kharkiv')
print(cities)