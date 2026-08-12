list_ = ["Collo", "Collo", "Mark", "Collo", "Lucy", "Collo", "Mark"]

record_dict = {}

for name in list_:
    record_dict[name] = record_dict.get(name, 0) + 1

# print(record_dict)

print('name is collo'.title())
print('name is collo'.upper())
print('name is collo'.capitalize())

print('name'.startswith('n'))

name = input('Input your name: ')
print(name)
from faker import Faker
fake = Faker()

print(fake.catch_phrase())
print(fake.sentence())