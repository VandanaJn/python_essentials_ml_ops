def flatten_recursive(nested, flat_list=None):
    if not flat_list:
        flat_list = []
    for it in nested:
        if isinstance(it, (str, bytes)):
            flat_list.append(it)
        elif isinstance(it, set):
            flatten_recursive(sorted(it, key=lambda x: str(x)), flat_list)
        elif hasattr(it, "__iter__"):
            flatten_recursive(it, flat_list)
        else:
            flat_list.append(it)
    return flat_list

def flatten(nested):
    flat_list = []
    stack = list(reversed(nested))
    while stack:
        it = stack.pop()
        if isinstance(it, (str, bytes)):
            flat_list.append(it)
        elif hasattr(it, "__iter__"):
            if isinstance(it, set):
                stack.extend(sorted(it, key=lambda x: str(x)))
            elif isinstance(it, dict):
                stack.extend(reversed(list(it.items())))
            else:
                stack.extend(reversed(it))
        else:
            flat_list.append(it)
    return flat_list


# print(flatten(nested_list))
