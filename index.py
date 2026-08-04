list_ = ["Collo", "Collo", "Mark", "Collo", "Lucy", "Collo", "Mark"]

record_dict = {}

for name in list_:
    record_dict[name] = record_dict.get(name, 0) + 1

print(record_dict)