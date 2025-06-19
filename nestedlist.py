nested_list = [{"a":"b"},1, [2, [3, {4, 5,"text"}], 6], 7,(4,5)]
def flatten_r(nested, flat_list=None ):
    if not flat_list:
        flat_list=[]
    for it in nested:
        if isinstance(it,(str,bytes)):
            flat_list.append(it)
        elif hasattr(it, '__iter__'):
            flatten_r(it, flat_list)
        else:
            flat_list.append(it)
    return flat_list

print(flatten_r(nested_list))

nested_list = [{"a":"b"},1, [2, [3, {4, 5,"text"}], 6], 7,(4,5)]
def flatten(nested):
    flat_list=[]
    stack=list(reversed(nested))
    while stack:
        it=stack.pop()
        if isinstance(it, (str,bytes)):
            flat_list.append(it)
        elif hasattr(it, '__iter__'):
            if isinstance(it, set):
                stack.extend(it)
            elif isinstance(it, dict):
                stack.extend(reversed(it.values()))
                stack.extend(reversed(it.keys()))
            else:
                stack.extend(reversed(it))
        else:
            flat_list.append(it)
    return flat_list

print(flatten(nested_list))



