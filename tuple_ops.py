tuple1 = (1, 3, 2, 3, 2, 2)
print(tuple1.index(1))
print(tuple1.index(2))
try:
    print(tuple1.index(5))
except ValueError as e:
    print(e)
print(tuple1.count(2))
print(tuple1.count(1))
print(tuple1.count(5))


def search(collection: tuple, search_item):
    for item in collection:
        if item == search_item:
            return True
    return False


print(search(tuple1, 3))
print(search(tuple1, 7))
