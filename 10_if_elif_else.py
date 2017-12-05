age = 25

if age < 10:
    print("baby")
elif (age > 12) and (age < 20):
    print("teen")
else:
    print("adult")

print('-----------')

all_cars = ['zaz', 'lada', 'bmw', 'audi', 'subaru']
germany_cars = ['bmw', 'audi']

if 'zaz' in all_cars:
    print(True)
else:
    print(False)

for xx in all_cars:
    if xx in germany_cars:
        print(xx + str(True))
    else:
        print(xx + str(False))
