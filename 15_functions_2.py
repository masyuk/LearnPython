def create_record(name,phone, adress):
    record = {
        'name': name,
        'phone': phone,
        'address': adress
    }
    return record

user1 = create_record("Max", "+5455545", "str slkjfd")
user2 = create_record("Mux", "+542342545", "str slkjfd")

print(user1)
print(user2)


def give_award(medal, *persons):
    for per in persons:
        print("Towarish "+ per.title()+" nagrazgdaetsya " + medal)


give_award("Za zaslugi", "Petya", "Vasya")