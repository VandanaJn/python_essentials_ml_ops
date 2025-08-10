def linear_search(data, items):
    items_dict = {i: [] for i in items}
    for idx, element in enumerate(data):
        if element in items_dict:
            items_dict[element].append(idx)
    return items_dict
